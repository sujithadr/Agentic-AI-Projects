from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from agents.cleaner import AICleanerAgent
from agents.validator import AIValidatorAgent
from agents.enricher import AIEnricherAgent

class PipelineState(BaseModel):
    raw_text: str
    cleaned_text: str = ""
    validation_notes: str = ""
    enriched_text: str = ""

class CleaningPipeline:
    def __init__(self):
        self.cleaner = AICleanerAgent()
        self.validator = AIValidatorAgent()
        self.enricher = AIEnricherAgent()
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(PipelineState)

        # Node 1: Cleaning
        def cleaning_node(state: PipelineState) -> PipelineState:
            cleaned = self.cleaner.process_dataframe_text(state.raw_text)
            return PipelineState(raw_text=state.raw_text, cleaned_text=cleaned)

        # Node 2: Validation
        def validation_node(state: PipelineState) -> PipelineState:
            notes = self.validator.validate(state.cleaned_text)
            return PipelineState(**state.dict(), validation_notes=notes)

        # Node 3: Enrichment
        def enrichment_node(state: PipelineState) -> PipelineState:
            enriched = self.enricher.enrich(state.cleaned_text)
            return PipelineState(**state.dict(), enriched_text=enriched)

        # Add nodes
        graph.add_node("cleaning", cleaning_node)
        graph.add_node("validation", validation_node)
        graph.add_node("enrichment", enrichment_node)

        # Add edges (flow)
        graph.set_entry_point("cleaning")
        graph.add_edge("cleaning", "validation")
        graph.add_edge("validation", "enrichment")
        graph.add_edge("enrichment", END)

        return graph.compile()

    def run_pipeline(self, raw_df_text: str) -> PipelineState:
        initial_state = PipelineState(raw_text=raw_df_text)
        result = self.graph.invoke(initial_state)
        return PipelineState(**result) if isinstance(result, dict) else result
