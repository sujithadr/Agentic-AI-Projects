import os
import pandas as pd
import requests
from sqlalchemy import create_engine

# Get the base directory dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")

class DataIngestion:
    def __init__(self, db_url=None):
        """Initialize data ingestion with an optional database connection."""
        self.engine = create_engine(db_url) if db_url else None

    ### ===== 1️⃣ LOAD DATA FROM CSV ===== ###
    def load_csv(self, file_name):
        """Loads a CSV file into a DataFrame"""
        file_path = os.path.join(DATA_DIR, file_name)
        try:
            df = pd.read_csv(file_path)
            print(f"✅ CSV Loaded Successfully: {file_path}")
            return df
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return None

    ### ===== 2️⃣ LOAD DATA FROM EXCEL ===== ###
    def load_excel(self, file_name, sheet_name=0):
        """Loads an Excel file into a DataFrame"""
        file_path = os.path.join(DATA_DIR, file_name)
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"✅ Excel Loaded Successfully: {file_path}")
            return df
        except Exception as e:
            print(f"❌ Error loading Excel: {e}")
            return None

    ### ===== 3️⃣ CONNECT TO DATABASE ===== ###
    def connect_database(self, db_url):
        """Establishes a database connection"""
        try:
            self.engine = create_engine(db_url)
            print("✅ Database Connection Successful")
        except Exception as e:
            print(f"❌ Error connecting to database: {e}")

    ### ===== 4️⃣ LOAD DATA FROM DATABASE ===== ###
    def load_from_database(self, query):
        """Fetches data from a database using a SQL query"""
        if self.engine is None:
            print("❌ No database connection. Call connect_database() first.")
            return None
        try:
            df = pd.read_sql(query, self.engine)
            print("✅ Data Loaded from Database Successfully")
            return df
        except Exception as e:
            print(f"❌ Error loading data from database: {e}")
            return None

    ### ===== 5️⃣ FETCH DATA FROM API ===== ###
    def fetch_from_api(self, api_url, params=None):
        """Fetches data from an API and returns it as a DataFrame"""
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data)
                print("✅ Data Fetched from API Successfully")
                return df
            else:
                print(f"❌ API Request Failed: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error fetching data from API: {e}")
            return None

# ======= TESTING THE CODE =======
if __name__ == "__main__":
    # 🔹 Set up database URL (Modify as needed)
    DB_USER = "postgres"
    DB_PASSWORD = "admin"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "demodb"

    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    ingestion = DataIngestion(DB_URL)

    ## === CSV TEST === ##
    df_csv = ingestion.load_csv("sample_data.csv")
    if df_csv is not None:
        print(df_csv.head())

    ## === EXCEL TEST === ##
    df_excel = ingestion.load_excel("sample_data.xlsx")
    if df_excel is not None:
        print(df_excel.head())

    ## === DATABASE TEST === ##
    ingestion.connect_database(DB_URL)
    df_db = ingestion.load_from_database("SELECT * FROM my_table")  # Change table name
    if df_db is not None:
        print(df_db.head())

    ## === API TEST === ##
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    df_api = ingestion.fetch_from_api(API_URL)
    if df_api is not None:
        print(df_api.head())
