import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Set it in the .env file.")

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)

class EnrichmentState(BaseModel):
    cleaned_text: str
    enriched_response: str = ""

class AIEnricherAgent:
    def __init__(self):
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(EnrichmentState)

        def enrich_logic(state: EnrichmentState) -> EnrichmentState:
            prompt = f"""You are a data enrichment assistant.

Given the following cleaned dataset:
{state.cleaned_text}

Perform enrichment:
- Expand abbreviations or codes (e.g., country code 'DE' → 'Germany')
- Add inferred fields where possible (e.g., city → country)
- Improve clarity and contextual quality

Return only the enriched dataset in CSV format.
"""
            enriched = llm.invoke(prompt)
            return EnrichmentState(
                cleaned_text=state.cleaned_text,
                enriched_response=enriched
            )

        graph.add_node("enrich", enrich_logic)
        graph.set_entry_point("enrich")
        graph.add_edge("enrich", END)

        return graph.compile()

    def enrich(self, cleaned_csv_text: str) -> str:
        """Run enrichment logic on cleaned AI CSV output."""
        state = EnrichmentState(cleaned_text=cleaned_csv_text)
        response = self.graph.invoke(state)

        if isinstance(response, dict):
            response = EnrichmentState(**response)

        return response.enriched_response.strip()
