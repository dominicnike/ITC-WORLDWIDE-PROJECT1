import requests
import pyodbc
import json

def fetch_api_data():
    url = "https://api.example.com/data"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    response = requests.get(url, headers=headers)
    return response.json()

def save_to_azure_sql(data):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=yourserver.database.windows.net;'
        'DATABASE=yourdb;UID=youruser;PWD=yourpassword'
    )
    cursor = conn.cursor()
    for record in data:
        cursor.execute("INSERT INTO YourTable (Column1, Column2) VALUES (?, ?)", record['field1'], record['field2'])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    data = fetch_api_data()
    save_to_azure_sql(data)