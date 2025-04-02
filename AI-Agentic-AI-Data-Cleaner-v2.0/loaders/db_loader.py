import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

class DBLoader:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine: Engine = create_engine(db_url)

    def load(self, query: str) -> pd.DataFrame:
        """Executes a SQL query and returns the result as a DataFrame."""
        try:
            df = pd.read_sql(query, self.engine)
            print("✅ Data loaded from database successfully.")
            return df
        except Exception as e:
            print(f"❌ Failed to load data from database: {e}")
            raise
