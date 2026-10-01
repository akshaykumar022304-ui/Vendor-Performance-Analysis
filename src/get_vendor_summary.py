# This is a script mainly to do tasks that need to be repeated again and again.
# In this example, we need to repeat the main tasks.

import sqlite3
import pandas as pd
import logging
from pathlib import Path
from ingestion_db import ingest_db

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "inventory.db"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a",
    force=True
)


def create_vendor_summary(conn):
    """
    This function will merge the different tables to get the
    overall vendor summary and add new columns in the resultant data.
    """

    vendor_sales_summary = pd.read_sql_query(
        """
        WITH FreightSummary AS (
            SELECT
                VendorNumber,
                SUM(Freight) AS FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),

        PurchaseSummary AS (
            SELECT
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price,
                pp.Volume
        ),

        SalesSummary AS (
            SELECT
                VendorNo,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesDollars) AS TotalSalesDollars,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        )

        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNo
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        """,
        conn
    )

    return vendor_sales_summary


def clean_data(df):
    """
    This function will clean the data.
    """

    # Changing datatype to float
    df["Volume"] = df["Volume"].astype("float")

    # Filling missing values with 0
    df.fillna(0, inplace=True)

    # Removing spaces from categorical columns
    df["VendorName"] = df["VendorName"].str.strip()
    df["Description"] = df["Description"].str.strip()

    # Creating new columns for better analysis
    df["GrossProfit"] = (
        df["TotalSalesDollars"]
        - df["TotalPurchaseDollars"]
    )

    df["ProfitMargin"] = (
    df["GrossProfit"]
    .div(df["TotalSalesDollars"].replace(0, pd.NA))
    .mul(100)
    )
   
    df["StockTurnover"] = (
    df["TotalSalesQuantity"]
    .div(df["TotalPurchaseQuantity"].replace(0, pd.NA))
    )

    df["SalesToPurchaseRatio"] = (
    df["TotalSalesDollars"]
    .div(df["TotalPurchaseDollars"].replace(0, pd.NA))
)

    return df


if __name__ == "__main__":

    # Creating database connection
    conn = sqlite3.connect(DB_PATH)

    logging.info("Creating Vendor Summary Table.....")

    summary_df = create_vendor_summary(conn)

    logging.info(summary_df.head())

    logging.info("Cleaning data...")

    clean_df = clean_data(summary_df)

    logging.info(clean_df.head())

    logging.info("Ingesting data...")

    ingest_db(
        clean_df,
        "vendor_sales_summary",
        conn
    )

    logging.info("Completed")