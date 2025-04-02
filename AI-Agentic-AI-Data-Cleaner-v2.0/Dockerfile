# Use an official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Expose ports
EXPOSE 8000 8501

# Run both FastAPI and Streamlit via shell script or entrypoint
CMD ["bash", "-c", "uvicorn services.clean_service:app --host 0.0.0.0 --port 8000 & streamlit run app/app.py --server.port=8501"]
