import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Set it in the .env file.")

# LangChain LLM setup
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

# Pydantic model for AI state
class CleaningState(BaseModel):
    input_text: str
    structured_response: str = ""

class AICleanerAgent:
    def __init__(self):
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(CleaningState)

        def clean_logic(state: CleaningState) -> CleaningState:
            response = llm.invoke(state.input_text)
            return CleaningState(
                input_text=state.input_text,
                structured_response=response
            )

        graph.add_node("cleaning", clean_logic)
        graph.set_entry_point("cleaning")
        graph.add_edge("cleaning", END)

        return graph.compile()

    def process_dataframe(self, df: pd.DataFrame, batch_size: int = 20) -> str:
        """Send data to AI in batches, collect structured cleaned results."""
        cleaned_outputs = []

        for i in range(0, len(df), batch_size):
            df_batch = df.iloc[i:i + batch_size]
            prompt = f"""You are a data cleaning assistant.

Analyze and clean the following dataset:
{df_batch.to_string(index=False)}

Instructions:
- Handle missing values with appropriate strategies
- Remove duplicates
- Standardize inconsistent formatting
- Output cleaned data in CSV format (no explanation)

"""
            state = CleaningState(input_text=prompt)
            response = self.graph.invoke(state)

            if isinstance(response, dict):
                response = CleaningState(**response)

            cleaned_outputs.append(response.structured_response.strip())

        return "\n".join(cleaned_outputs)
