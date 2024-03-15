from pydantic import BaseModel


class PipelineConfig(BaseModel):
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    vector_store: str = "chroma"
    retrieval_top_k: int = 5
    max_concurrent_agents: int = 4


DEFAULT_CONFIG = PipelineConfig()


