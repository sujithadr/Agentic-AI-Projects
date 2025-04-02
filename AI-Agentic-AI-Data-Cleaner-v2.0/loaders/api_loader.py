import pandas as pd
import requests

class APILoader:
    def __init__(self, api_url: str, params: dict = None):
        self.api_url = api_url
        self.params = params or {}

    def load(self) -> pd.DataFrame:
        """Fetches data from an API and returns it as a DataFrame."""
        try:
            response = requests.get(self.api_url, params=self.params)
            response.raise_for_status()

            data = response.json()

            # Attempt to normalize nested JSON if needed
            if isinstance(data, dict):
                data = [data]
            elif isinstance(data, list) and isinstance(data[0], dict):
                pass
            else:
                raise ValueError("API response is not in expected format")

            df = pd.DataFrame(data)
            print("✅ Data fetched from API successfully.")
            return df

        except Exception as e:
            print(f"❌ Failed to fetch data from API: {e}")
            raise
