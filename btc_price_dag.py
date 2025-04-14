
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging
import btc_price_scraper

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_scraper():
    try:
        logging.info("Starting Bitcoin price scraper...")
        price = btc_price_scraper.fetch_btc_price()
        if price:
            logging.info(f"Fetched Bitcoin price: {price}")
            btc_price_scraper.save_to_azure_sql(price)
            logging.info("Saved Bitcoin price to Azure SQL.")
        else:
            logging.warning("Failed to fetch Bitcoin price.")
    except Exception as e:
        logging.error(f"Error in run_scraper: {e}")
        raise

dag = DAG(
    'btc_price_scraper',
    default_args=default_args,
    description='Scrape Bitcoin price and store in Azure SQL',
    schedule_interval='@hourly',  # Corrected to schedule_interval
    catchup=False,
)

task = PythonOperator(
    task_id='scrape_and_store_btc_price',
    python_callable=run_scraper,
    dag=dag,
)
