# Vendor Performance Analysis

## Project Overview

This project analyzes vendor performance using purchasing, sales, inventory, and profitability data to identify business trends and opportunities for improving procurement and inventory management.

The project combines Python-based data analysis, SQL, statistical analysis, and an interactive Power BI dashboard to evaluate vendor contribution, purchasing efficiency, inventory turnover, sales performance, and profitability.

The workflow covers data ingestion, database processing, exploratory data analysis, data cleaning, feature engineering, statistical analysis, and dashboard development.

## Objectives

- Identify vendors and brands with the highest sales performance.
- Measure the contribution of top vendors to total procurement.
- Analyze whether bulk purchasing is associated with lower unit purchase prices.
- Identify vendors with low inventory turnover and potentially slow-moving inventory.
- Estimate capital tied up in unsold inventory.
- Compare profit margins between top-performing and low-performing vendors.
- Statistically test whether the difference in profit margins between vendor groups is significant.
- Build an interactive dashboard for visualizing vendor performance and procurement metrics.

## Project Workflow

```text
Raw CSV Data
     │
     ▼
Data Ingestion
     │
     ▼
SQLite Database
     │
     ▼
Vendor-Level Data Processing
     │
     ▼
Data Cleaning & EDA
     │
     ▼
Feature Engineering
     │
     ├── Unit Purchase Price
     ├── Order Size
     └── Unsold Inventory Value
     │
     ▼
Statistical & Business Analysis
     │
     ▼
Power BI Dashboard

Key Analysis:

1. Sales Performance

The analysis identifies the vendors and brands generating the highest total sales revenue.

The top 10 vendors account for a substantial share of total sales, with DIAGEO NORTH AMERICA INC generating approximately $67.99M in total sales in the analyzed dataset.

The highest-selling brands include:

-Jack Daniels No 7 Black
-Tito's Handmade Vodka
-Grey Goose Vodka
-Capt Morgan Spiced Rum
-Absolut 80 Proof
-Jameson Irish Whiskey
-Ketel One Vodka
-Baileys Irish Cream
-Kahlua
-Tanqueray

2. Procurement Concentration

The analysis measures how dependent total procurement is on the largest vendors.

The top 10 vendors account for 65.69% of total purchase contribution, indicating a significant concentration of procurement among a relatively small group of vendors.

3. Bulk Purchasing and Unit Cost

Purchase quantities are divided into Small, Medium, and Large order sizes using quantile-based grouping.

The average unit purchase prices observed were:

Order Size	Average Unit Purchase Price
Small	39.07
Medium	15.49
Large	10.78

Within this dataset, larger purchase quantities are associated with lower average unit purchase prices.

This analysis provides a basis for evaluating potential purchasing efficiencies while recognizing that the relationship is observational and does not by itself establish causation.

4. Inventory Turnover

Stock turnover is used to identify vendors with relatively slow-moving inventory.

Vendors with average stock turnover below 1 include:

-ALISA CARR BEVERAGES
-HIGHLAND WINE MERCHANTS LLC
-PARK STREET IMPORTS LLC
-Circa Wines
-Dunn Wine Brokers
-CENTEUR IMPORTS LLC
-SMOKY QUARTZ DISTILLERY LLC
-TAMWORTH DISTILLING
-THE IMPORTED GRAPE LLC
-WALPOLE MTN VIEW WINERY

A stock turnover below 1 indicates that sales quantity is lower than the corresponding purchased quantity within the analyzed records.

5. Unsold Inventory

Unsold inventory value is estimated using:

Unsold Inventory Value =
(Total Purchase Quantity - Total Sales Quantity) × Purchase Price

The vendors with the highest calculated unsold inventory value included:

Vendor	Unsold Inventory Value
DIAGEO NORTH AMERICA INC	$722.21K
JIM BEAM BRANDS COMPANY	$554.67K
PERNOD RICARD USA	$470.63K
WILLIAM GRANT & SONS INC	$401.96K
E & J GALLO WINERY	$228.28K

These values represent estimated capital tied up in unsold inventory based on the available purchase and sales quantities.

6. Profitability Analysis

Profit margins are compared between vendors in the upper and lower quartiles of total sales dollars.

The analysis uses:

-75th percentile of TotalSalesDollars to define the top-performing group.
-25th percentile of TotalSalesDollars to define the low-performing group.
-95% confidence intervals to estimate the mean profit margin for each group.
-Welch's two-sample t-test to test for a difference in mean profit margins.

The hypothesis test produced:

T-Statistic: -17.6695
P-Value: 0.0000

At a significance level of 0.05, the null hypothesis was rejected, indicating a statistically significant difference in mean profit margins between the two groups in this dataset.

Data Cleaning

The original vendor summary contained records with negative or zero values in important analytical fields.

Initial checks identified:

Total rows: 10,692
GrossProfit <= 0: 2,128
ProfitMargin <= 0: 1,950
TotalSalesQuantity <= 0: 178

Rather than removing observations solely because they appeared statistically extreme, the cleaning process focused on inconsistent records that could interfere with profitability and sales analysis.

Records with non-positive GrossProfit, ProfitMargin, or TotalSalesQuantity were excluded from the analytical dataset.

Extreme values in variables such as purchase price, freight cost, and stock turnover were retained because they may represent legitimate business cases such as premium products, bulk shipments, or unusual inventory movement.

Tools & Technologies:
-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
-SciPy
-SQL
-SQLite
-Jupyter Notebook
-Power BI
-Git
-GitHub

Vendor-Performance-Analysis/
│
├── dashboard/
│   └── Vendor_Performance_Dashboard.pbix
│
├── data/
│   └── vendor_performance_final.csv
│
├── notebooks/
│   ├── Vendor Performance Analysis.ipynb
│   └── Exploratory data analysis.ipynb
│
├── src/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── .gitignore
└── README.md
```

## Dashboard

The project includes an interactive Power BI dashboard designed to provide a visual overview of vendor sales, procurement, profitability, inventory, and purchasing performance.

The dashboard allows the analyzed vendor data to be explored through interactive visualizations and filters.

<img src="https://raw.githubusercontent.com/akshaykumar022304-ui/Vendor-Performance-Analysis/main/dashboard/dashboard_preview.png" alt="Vendor Performance Dashboard">

## Project Background

This project was initially developed by following a YouTube tutorial (Tech Classes - Vendor Performance Data Analysis)  to understand the fundamentals of vendor performance analysis, data ingestion, and business intelligence workflows.

The project was subsequently customized and extended with additional data analysis, feature engineering, statistical analysis, visualizations, documentation, and a Power BI dashboard to develop a more personalized end-to-end portfolio project.