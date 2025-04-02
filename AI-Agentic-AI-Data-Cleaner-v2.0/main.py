import pandas as pd
from rules.basic_rules import BasicRulesCleaner
from pipelines.clean_pipeline import CleaningPipeline

# Load local file (update path if needed)
CSV_FILE = "data/sample_data.csv"

# Step 1: Load raw data
df = pd.read_csv(CSV_FILE)
print("📂 Loaded raw data:")
print(df.head())

# Step 2: Apply rule-based cleaning
rule_cleaner = BasicRulesCleaner(missing_strategy="mean")
df_rule_cleaned = rule_cleaner.clean(df)
print("\n🧽 Rule-based cleaned data:")
print(df_rule_cleaned.head())

# Step 3: Run AI pipeline
pipeline = CleaningPipeline()
raw_text = df_rule_cleaned.to_csv(index=False)
result = pipeline.run_pipeline(raw_text)

# Step 4: Output results
print("\n✅ AI Cleaned Data:")
print(result.cleaned_text)

print("\n🔍 Validation Notes:")
print(result.validation_notes)

print("\n✨ Enriched Data:")
print(result.enriched_text)
