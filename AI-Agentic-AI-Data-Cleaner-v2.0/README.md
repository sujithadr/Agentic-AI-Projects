# 🧹 Data Cleaner Pro

An AI-powered data cleaning platform with modular architecture, supporting multiple data sources and agents for cleaning, validation, and enrichment.

---

## 🚀 Features

- ✅ Rule-based and AI-powered cleaning
- 📥 Load data from CSV, Excel, Database, or API
- 🧠 Multi-agent pipeline using LangGraph (Cleaner → Validator → Enricher)
- 🖥️ Streamlit UI + FastAPI backend
- 🐳 Docker & Docker Compose support for deployment

---

## 📦 Project Structure

```
data-cleaner-pro/
├── agents/              # AI agents (cleaner, validator, enricher)
├── loaders/             # CSV, DB, API loaders
├── pipelines/           # LangGraph pipeline
├── rules/               # Rule-based cleaning logic
├── services/            # FastAPI endpoints
├── app/                 # Streamlit frontend
├── main.py              # CLI runner
├── .env.template        # Env config
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container config
└── docker-compose.yml   # Multi-container orchestration
```

---

## 🧪 Run Locally (Without Docker)

### 1. 📥 Install Dependencies

```bash
python3.10 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. 🔐 Set Up `.env`

Create a `.env` file based on `.env.template` and add your OpenAI key:
```
OPENAI_API_KEY=your-key-here
```

### 3. 🚀 Start Services

Start the FastAPI backend:
```bash
uvicorn services.clean_service:app --reload
```

Start the Streamlit UI:
```bash
streamlit run app/app.py
```

---

## 🐳 Run With Docker

### 1. 🔐 Create `.env` (or rename `.env.template`)

```
OPENAI_API_KEY=your-key-here
```

### 2. 🏗️ Build and Start the Stack

```bash
docker-compose up --build
```

- FastAPI available at: http://localhost:8000/docs
- Streamlit UI at: http://localhost:8501

---

## ✨ Example Use Cases

- Clean messy survey data
- Validate API scraped results
- Standardize formats in user-uploaded Excel sheets
- Enrich datasets with missing context (e.g. country names)

---

## 📃 License

MIT License © Sujith Somanunnithan