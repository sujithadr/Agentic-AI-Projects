import pandas as pd
import os

class CSVLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        """Loads a CSV file into a DataFrame."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
        try:
            df = pd.read_csv(self.file_path)
            print(f"✅ CSV Loaded Successfully: {self.file_path}")
            return df
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            raise
