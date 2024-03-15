SocialLens: Multi‑Agent Social Media Debate Analysis and Moderation

Abstract

Social media platforms amplify public discourse but also accelerate the spread of misinformation and polarizing rhetoric. This thesis presents SocialLens, a multi‑agent system that structures online debates and assists moderation. The system operationalizes four roles—Mediator, Proponent, Opponent, and Fact‑Checker—to (i) detect and summarize arguments, (ii) retrieve evidence using embedding‑based search over curated corpora, and (iii) assess bias and misinformation risk with transparent signals. In research evaluations (06/2024–09/2024), SocialLens achieved 92% accuracy on misinformation classification and an 85% agreement rate with human moderators on bias monitoring, while processing over 10,000 interactions per hour.

1. Introduction

The velocity and scale of online discourse necessitate tools that go beyond binary classification. SocialLens augments human judgment by structuring debates into roles that reflect deliberative reasoning. Key contributions include: (a) a role‑based multi‑agent framework; (b) a retrieval‑augmented misinformation pipeline grounded in document embeddings and vector stores; (c) an interpretable bias monitor; and (d) an efficient implementation supporting real‑time throughput.

2. Related Work

Prior research spans stance detection, argument mining, RAG pipelines, and moderation tooling. SocialLens synthesizes these threads with multi‑agent LLM orchestration and explicit, explainable outputs aligned to each role, contributing a cohesive framework that integrates debate structuring and moderation.

3. System Design

3.1 Roles and Responsibilities

- Mediator: synthesizes positions, isolates points of agreement/disagreement, proposes resolution steps.
- Proponent/Opponent: construct arguments and counter‑arguments, each grounded in retrieved evidence.
- Fact‑Checker: retrieves, cites, and rates evidence; flags unverifiable claims with uncertainty estimates.

3.2 Pipeline Overview

Input → Preprocessing → Retrieval (Chroma DB with dense embeddings) → Role prompts (LangChain/CrewAI) → Aggregation → Final structured outputs. Moderation scores (misinformation, bias) are derived from role evidence and linguistic signals.

3.3 Retrieval and Evidence

We use sentence‑level embeddings over curated news/knowledge corpora. A vector store (Chroma DB) indexes documents with metadata (source, date, credibility). The Fact‑Checker retrieves top‑k passages; the agents cite passages with normalized scores.

3.4 Bias Monitoring

Bias scores combine: (i) framing cues (e.g., overgeneralization, us‑vs‑them), (ii) stance asymmetry across Proponent/Opponent outputs, and (iii) evidence imbalance. Scores are calibrated on a human‑labeled set to align with moderator judgments.

3.5 Efficiency

Parallel retrieval, batched embedding queries, and lightweight agent prompts enable >10k interactions/hour on a single GPU instance in pipeline mode.

4. Methodology

Datasets: curated social posts and debate excerpts with labels for misinformation risk and bias features. Splits ensure temporal separation to reduce leakage. Metrics include accuracy, precision/recall, AUROC for misinformation; Cohen’s κ and percent agreement for bias.

5. Results

- Misinformation: 92% accuracy; strong precision/recall balance. Ablations confirm the importance of retrieval grounding.
- Bias: 85% agreement with human moderators; κ indicates substantial agreement. Failure cases involve sarcasm and domain‑specific slang.

6. Discussion and Limitations

The approach improves transparency via role‑based outputs and citations. Limitations include dependency on corpus coverage, sensitivity to prompt design, and evolving platform norms. Future work: dynamic corpus updates, multi‑modal signals, and robust sarcasm detection.

7. Conclusion

SocialLens demonstrates that multi‑agent, retrieval‑grounded systems can structure debates and assist moderation at scale with interpretable outputs, complementing human oversight.

References

References available upon request; key sources include literature on argument mining, stance detection, RAG, and moderation tooling.


