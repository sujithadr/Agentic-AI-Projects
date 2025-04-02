import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langgraph.graph import StateGraph, END
from pydantic import BaseModel

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Set it in the .env file.")

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

class ValidationState(BaseModel):
    cleaned_text: str
    validation_feedback: str = ""

class AIValidatorAgent:
    def __init__(self):
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(ValidationState)

        def validate_logic(state: ValidationState) -> ValidationState:
            prompt = f"""You are a data quality validator.

Review the following cleaned data:
{state.cleaned_text}

Check for:
- Column consistency (data types, units)
- Invalid values or obvious errors
- Outliers or formatting issues

Output your validation notes clearly in bullet points.
"""
            feedback = llm.invoke(prompt)
            return ValidationState(
                cleaned_text=state.cleaned_text,
                validation_feedback=feedback
            )

        graph.add_node("validate", validate_logic)
        graph.set_entry_point("validate")
        graph.add_edge("validate", END)

        return graph.compile()

    def validate(self, cleaned_csv_text: str) -> str:
        """Run validator logic on cleaned AI CSV output."""
        state = ValidationState(cleaned_text=cleaned_csv_text)
        response = self.graph.invoke(state)

        if isinstance(response, dict):
            response = ValidationState(**response)

        return response.validation_feedback.strip()
