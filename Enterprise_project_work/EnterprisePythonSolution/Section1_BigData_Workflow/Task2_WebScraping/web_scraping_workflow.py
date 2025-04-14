from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def scrape_bitcoin_price():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    price_tag = soup.find("div", class_="priceValue")
    price = price_tag.text.strip().replace("$", "").replace(",", "")
    data = {"timestamp": [datetime.utcnow()], "price": [float(price)]}
    df = pd.DataFrame(data)
    df.to_csv("/path/to/output.csv", index=False)

dag = DAG(
    'web_scraping_workflow',
    default_args=default_args,
    description='Automated Web Scraping Workflow',
    schedule_interval='@hourly',
    catchup=False,
)

task = PythonOperator(
    task_id='scrape_bitcoin_price',
    python_callable=scrape_bitcoin_price,
    dag=dag,
)