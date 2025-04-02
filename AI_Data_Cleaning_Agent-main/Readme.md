# 🧹 AI-Powered Data Cleaning System

##  Overview
The **AI-Powered Data Cleaning System** is a **Streamlit + FastAPI + AI** application that automates data cleaning using **rule-based** and **AI-powered techniques**. It supports data ingestion from **CSV/Excel files, Database queries, and API endpoints** and processes them using **LangChain AI agents** to enhance data quality.

##  Features

- ✅ **Multi-source Data Ingestion**: Supports CSV/Excel, SQL queries, and API endpoints.
- ✅ **AI-driven Data Cleaning**: Uses LangChain AI Agents for intelligent cleaning.
- ✅ **Rule-based Data Preprocessing**: Handles missing values, duplicates, and formatting.
- ✅ **Web UI with Streamlit**: A user-friendly interface for data selection and preview.
- ✅ **FastAPI Backend**: Handles requests and integrates AI-based transformations.
- ✅ **Real-time Processing**: Instant feedback and preview of cleaned data.



## Project Structure
```
├── app/
│   ├── app.py               # Streamlit web application
│
├── scripts/
│   ├── ai_agents.py         # AI-powered data cleaning using OpenAI API
│   ├── backend.py           # FastAPI backend for data processing
│   ├── data_cleaning.py     # Rule-based data cleaning functions
│   ├── data_ingestion.py    # Data loading from various sources
│
├── main.py                  # Main script to run the data processing pipeline
├── requirements.txt         # Dependencies list
├── README.md                # Documentation
├── .env                     # Environment variables (API keys)
```

---

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8).

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/sujithadr/AI_Data_Cleaning_Agent-main.git
cd data-cleaning-framework
```

### 2️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables:
Create a `.env` file and add the OpenAI API key:
```sh
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

### 🏗️ Run the FastAPI Backend
```sh
uvicorn scripts.backend:app --reload
```
Access it at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 🖥️ Run the Streamlit Web App
```sh
streamlit run app/app.py
```

### 🏃 Run the Main Processing Script
```sh
python main.py
```

---

## API Endpoints
| Endpoint          | Method | Description |
|------------------|--------|-------------|
| `/clean-data`    | POST   | Upload CSV/Excel for cleaning |
| `/clean-db`      | POST   | Process data from a database |
| `/clean-api`     | GET    | Fetch data from an API and clean it |

---

## Functionality Breakdown

### **1️⃣ Data Ingestion (`scripts/data_ingestion.py`)**
- Load data from **CSV, Excel, Databases, APIs**.
- Handles various file formats and structured sources.

### **2️⃣ Rule-Based Cleaning (`scripts/data_cleaning.py`)**
- **Handle Missing Values**: Replace with mean/median/mode or drop rows.
- **Remove Duplicates**: Deduplicate dataset.
- **Fix Data Types**: Convert columns to appropriate formats.

### **3️⃣ AI-Powered Cleaning (`scripts/ai_agents.py`)**
- Uses OpenAI's **GPT models** for intelligent data cleaning.
- Can detect and correct errors based on textual descriptions.

### **4️⃣ FastAPI Backend (`scripts/backend.py`)**
- API endpoints for data ingestion and cleaning.
- Processes user-uploaded files, database queries, and API responses.

### **5️⃣ Streamlit Web App (`app/app.py`)**
- Interactive web interface for data upload and cleaning.
- Visual representation of cleaned data.

---

## Contributing
Feel free to submit **issues, feature requests, or pull requests**!

---

## License
This project is licensed under the **MIT License**.

---

## Authors
- Sujith Somanunnithan - [GitHub Profile](https://github.com/sujithadr)







