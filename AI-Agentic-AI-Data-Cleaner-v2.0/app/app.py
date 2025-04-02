import streamlit as st
import pandas as pd
import requests
import json
from io import StringIO

# Backend URL
API_URL = "http://127.0.0.1:8000/clean"

st.set_page_config(page_title="Data Cleaner Pro", layout="wide")

# Header
st.title("🧹 Data Cleaner Pro")
st.markdown("*AI-powered data cleaning, validation, and enrichment*")

# File Upload
uploaded_file = st.file_uploader("📂 Upload CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    
    if file_ext == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df)

    if st.button("🚀 Clean with AI"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()

            st.subheader("✅ Cleaned Data")
            st.dataframe(pd.read_csv(StringIO(result["cleaned_data"])))

            st.subheader("🔍 Validation Notes")
            st.markdown(result["validation_notes"])

            st.subheader("✨ Enriched Data")
            st.dataframe(pd.read_csv(StringIO(result["enriched_data"])))

        else:
            st.error(f"❌ Error: {response.json()['detail']}")
