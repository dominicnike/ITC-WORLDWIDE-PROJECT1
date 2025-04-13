
import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime

def fetch_btc_price():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        price_tag = soup.find("div", class_="priceValue")
        price = price_tag.text.strip().replace("$", "").replace(",", "")
        return float(price)
    except Exception as e:
        print("Error fetching price:", e)
        return None

def save_to_azure_sql(price):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=yourserver.database.windows.net;'
        'DATABASE=yourdb;UID=youruser;PWD=yourpassword')
    
    cursor = conn.cursor()
    timestamp = datetime.datetime.utcnow()
    cursor.execute("INSERT INTO BitcoinPrice (PriceUSD, TimestampUTC) VALUES (?, ?)", price, timestamp)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    price = fetch_btc_price()
    if price:
        save_to_azure_sql(price)
        print(f"Saved Bitcoin price: ${price}")
