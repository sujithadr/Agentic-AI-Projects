import io
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pipelines.clean_pipeline import CleaningPipeline

app = FastAPI(title="Data Cleaner Pro API")

# Enable CORS for frontend (e.g., Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = CleaningPipeline()

@app.post("/clean")
async def clean_data(file: UploadFile = File(...)):
    """Upload CSV/Excel and return cleaned, validated, enriched data."""
    try:
        file_ext = file.filename.split(".")[-1].lower()
        content = await file.read()

        # Load file into DataFrame
        if file_ext == "csv":
            df = pd.read_csv(io.StringIO(content.decode("utf-8")))
        elif file_ext in ("xls", "xlsx"):
            df = pd.read_excel(io.BytesIO(content))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type.")

        # Convert to CSV text for AI agent processing
        raw_text = df.to_csv(index=False)
        result = pipeline.run_pipeline(raw_text)

        return {
            "cleaned_data": result.cleaned_text,
            "validation_notes": result.validation_notes,
            "enriched_data": result.enriched_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {e}")
