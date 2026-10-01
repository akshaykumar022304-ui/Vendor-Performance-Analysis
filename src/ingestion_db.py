import pandas as pd
import os 
from sqlalchemy import create_engine
import logging 
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Data"
DB_PATH = BASE_DIR / "inventory.db"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig( 
    filename = LOG_DIR / "ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force = True
   
)

engine = create_engine(f"sqlite:///{DB_PATH}")

def ingest_db(df , table_name, engine):
    '''a function to injest dataframe to database table''' 
    df.to_sql(table_name, con = engine , if_exists = 'replace', index = False )

def load_raw_data():
    ''' this function will load CSVs as dataframe and ingest into db'''
    start = time.time()

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")
            
    csv_files = [file for file in os.listdir(DATA_DIR) if file.endswith('.csv')]

    logging.info(f"Found {len(csv_files)} CSV files for ingestion")

    for file in csv_files:
        df = pd.read_csv(DATA_DIR / file)
        logging.info(f"Ingesting {file} into database")
        ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logging.info('------------------Ingestion complete----------------')
    
    logging.info(f'Total time taken: {total_time} minutes')

if __name__== '__main__':
    load_raw_data()