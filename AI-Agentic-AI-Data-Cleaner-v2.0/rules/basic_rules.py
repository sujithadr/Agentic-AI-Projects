
import pandas as pd
import numpy as np

class BasicRulesCleaner:
    def __init__(self, missing_strategy="mean"):
        self.missing_strategy = missing_strategy

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fill or drop missing values based on the selected strategy."""
        if self.missing_strategy == "mean":
            return df.fillna(df.mean(numeric_only=True))
        elif self.missing_strategy == "median":
            return df.fillna(df.median(numeric_only=True))
        elif self.missing_strategy == "mode":
            return df.fillna(df.mode().iloc[0])
        elif self.missing_strategy == "drop":
            return df.dropna()
        else:
            raise ValueError(f"Unknown missing value strategy: {self.missing_strategy}")

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicated rows."""
        return df.drop_duplicates()

    def fix_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
        """Try converting columns to numeric types where possible."""
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except Exception:
                pass  # Leave column unchanged if conversion fails
        return df

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply all rule-based cleaning steps."""
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.fix_data_types(df)
        return df
