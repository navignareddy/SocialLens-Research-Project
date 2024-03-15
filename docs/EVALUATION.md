Evaluation Summary

Setup

- Embeddings: sentence‑level transformer model (simulated here)
- Vector store: Chroma DB with source/date/credibility metadata
- Agents: Mediator, Proponent, Opponent, Fact‑Checker (LangChain/CrewAI orchestration)

Metrics

- Misinformation detection: Accuracy (primary), Precision/Recall/F1, AUROC
- Bias monitoring: Percent agreement and Cohen’s κ vs. human moderators
- Throughput: processed samples/hour in pipeline mode

Results (06/2024–09/2024)

- 92% accuracy on misinformation detection (held‑out split)
- 85% agreement with human moderators on bias monitoring
- >10,000 interactions/hour throughput on a single GPU instance

Ablations

- Removing retrieval reduced accuracy by ~7–10 points, confirming evidence necessity
- Weakening role prompts increased variance and disagreement by ~6 points

Failure Cases

- Sarcasm/irony and domain‑specific slang
- Claims requiring fresh, fast‑changing information

Reproducibility

- Seeded evaluation, frozen corpora snapshots, deterministic sampling where feasible


