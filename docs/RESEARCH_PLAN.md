Research Plan (Mar–Sep 2024)

Objectives

- Design a multi‑agent framework for debate structuring and moderation
- Build a retrieval‑augmented misinformation pipeline (embeddings + Chroma DB)
- Implement bias monitoring aligned with human moderator judgments
- Evaluate accuracy, agreement, and throughput

Timeline

- March 2024: Problem framing, dataset curation, baseline heuristics
- April 2024: Embedding selection, Chroma DB integration, retrieval evaluation
- May 2024: Agent role prompts, orchestration via LangChain/CrewAI
- June 2024: End‑to‑end pipeline v1, early metrics
- July 2024: Calibration and ablations
- August 2024: Bias agreement study with human moderators
- September 2024: Final evaluation, documentation, and release

Methodology

- Data: public posts and debate excerpts; de‑identified and cleaned
- Retrieval: dense embeddings, cosine similarity, source credibility metadata
- Agents: Mediator, Proponent, Opponent, Fact‑Checker; short, role‑specific prompts
- Metrics: accuracy, F1, AUROC (misinformation); κ and percent agreement (bias); throughput

Risks and Mitigations

- Corpus coverage gaps → frequent updates, diverse sources
- Prompt sensitivity → few‑shot exemplars, prompt audits
- Ambiguous labels → double‑annotation, adjudication protocol


