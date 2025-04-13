
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import btc_price_scraper

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_scraper():
    price = btc_price_scraper.fetch_btc_price()
    if price:
        btc_price_scraper.save_to_azure_sql(price)

dag = DAG(
    'btc_price_scraper',
    default_args=default_args,
    description='Scrape Bitcoin price and store in Azure SQL',
    schedule_interval='@hourly',
    catchup=False,
)

task = PythonOperator(
    task_id='scrape_and_store_btc_price',
    python_callable=run_scraper,
    dag=dag,
)
