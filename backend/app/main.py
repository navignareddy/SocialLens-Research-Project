from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from .pipeline import retrieve_evidence, run_agents_with_evidence


class TextRequest(BaseModel):
    text: str


class MisinformationResponse(BaseModel):
    score: float
    verdict: str
    evidence: List[str]
    explanation: str


class BiasResponse(BaseModel):
    bias_score: float
    labels: List[str]
    reasoning: str


class DebateResponse(BaseModel):
    mediator_summary: str
    proponent: str
    opponent: str
    fact_checker: str


app = FastAPI(title="SocialLens API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def simple_misinformation_score(text: str) -> float:
    keywords = [
        "miracle cure",
        "guaranteed",
        "secret",
        "100%",
        "hoax",
        "fake",
        "exposed",
    ]
    score = 0.0
    lowered = text.lower()
    for word in keywords:
        if word in lowered:
            score += 0.15
    score = min(1.0, score)
    return score


def simple_bias_detection(text: str) -> (float, List[str]):
    labels: List[str] = []
    lowered = text.lower()
    if any(x in lowered for x in ["always", "never", "everyone", "no one"]):
        labels.append("overgeneralization")
    if any(x in lowered for x in ["obviously", "clearly", "undeniably"]):
        labels.append("assertion bias")
    if any(x in lowered for x in ["they", "them", "those people"]):
        labels.append("us-vs-them framing")
    bias_score = min(1.0, 0.2 * len(labels))
    return bias_score, labels


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/analyze/misinformation", response_model=MisinformationResponse)
def analyze_misinformation(req: TextRequest):
    score = simple_misinformation_score(req.text)
    verdict = "likely" if score >= 0.6 else ("uncertain" if score >= 0.3 else "unlikely")
    evidence = []
    for kw in ["miracle cure", "guaranteed", "secret", "hoax", "fake", "exposed"]:
        if kw in req.text.lower():
            evidence.append(f"keyword: {kw}")
    explanation = (
        "Heuristic score based on sensational or absolute keywords. "
        "Replace with embedding-based retrieval and fact-checking chains in production."
    )
    return MisinformationResponse(score=score, verdict=verdict, evidence=evidence, explanation=explanation)


@app.post("/api/moderation/bias", response_model=BiasResponse)
def analyze_bias(req: TextRequest):
    bias_score, labels = simple_bias_detection(req.text)
    reasoning = "Detected stylistic and framing cues correlated with biased rhetoric."
    return BiasResponse(bias_score=bias_score, labels=labels, reasoning=reasoning)


@app.post("/api/debate/structure", response_model=DebateResponse)
def structure_debate(req: TextRequest):
    text = req.text.strip()
    evidence = retrieve_evidence(text, top_k=3)
    agent_outputs = run_agents_with_evidence(text, evidence)
    proponent = f"Proponent: {agent_outputs['proponent']}"
    opponent = f"Opponent: {agent_outputs['opponent']}"
    fact_checker = f"Fact-Checker: {agent_outputs['fact_checker']}\nCitations: " + ", ".join(agent_outputs["citations"]) if agent_outputs.get("citations") else f"Fact-Checker: {agent_outputs['fact_checker']}"
    mediator_summary = (
        "Mediator: Synthesizes positions, enumerates agreements/disagreements, and requests further verification where needed."
    )
    return DebateResponse(
        mediator_summary=mediator_summary,
        proponent=proponent,
        opponent=opponent,
        fact_checker=fact_checker,
    )


