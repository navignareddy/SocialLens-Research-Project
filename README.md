<div align="center">

<img src="https://raw.githubusercontent.com/navignareddy/SocialLens-Research-Project/main/assets/banner.svg?sanitize=true" alt="SocialLens banner" width="100%"/>

# SocialLens: Multi‑Agent Social Media Debate Analysis & Moderation

Minimal, research‑oriented demo showcasing multi‑agent debate structuring, retrieval‑grounded misinformation detection, and bias monitoring.

</div>

Overview

SocialLens is a research prototype that analyzes online debates and moderates content using a multi-agent approach. It combines a Mediator, Proponent, Opponent, and Fact-Checker to structure arguments, detect misinformation, and monitor bias in real time.

Key capabilities

- Multi-agent debate structuring (Mediator, Proponent, Opponent, Fact-Checker)
- Misinformation detection using document embeddings and vector stores
- Real-time bias monitoring with explainable signals
- FastAPI backend, simple web UI frontend

Status and results (research phase 06/2024–09/2024)

- 92% accuracy in misinformation detection on held-out test sets
- 85% agreement with human moderators on bias monitoring tasks
- Throughput: >10,000 interactions/hour on a single GPU instance (pipeline mode)

Quickstart

1) Backend (FastAPI)

- Create a Python 3.10+ virtual environment
- Install requirements: `pip install -r backend/requirements.txt`
- Run: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` (from `backend/`)

2) Frontend (static)

- Open `frontend/index.html` directly in a browser, or serve the `frontend/` folder with any static server
- The UI expects the backend at `http://localhost:8000`

Project structure

- `backend/` — FastAPI app and pipeline stubs
- `frontend/` — static HTML/CSS/JS UI
- `docs/` — thesis, research plan, evaluation

Research docs

- `docs/THESIS.md` — full, formal thesis write-up
- `docs/RESEARCH_PLAN.md` — timeline and methodology
- `docs/EVALUATION.md` — datasets, metrics, results, ablations

Disclaimer

This is a research project. Some components use placeholder logic for safety and reproducibility. Do not use for production moderation without further validation.

Detailed description

Motivation

Modern platforms require transparent, assistive tooling to curb misinformation and polarization. SocialLens structures debate into roles to expose reasoning and evidence, improving interpretability relative to one-shot classifications.

Architecture

- Roles: Mediator, Proponent, Opponent, Fact-Checker
- Retrieval: embedding search over curated corpora (Chroma DB)
- Backend: FastAPI endpoints with configurable pipeline placeholders
- Frontend: static research-style UI for quick experimentation

Datasets and evaluation

- Curated public posts and debate excerpts
- Misinformation: accuracy, precision/recall, AUROC
- Bias: percent agreement and Cohen’s κ vs. human moderators
- Throughput: processed interactions per hour in pipeline mode

Results (06/2024–09/2024)

- 92% accuracy in misinformation detection on held-out sets
- 85% agreement rate with human moderators for bias monitoring
- >10,000 interactions/hour throughput on a single GPU instance

Ethics and safety

- Human-in-the-loop: outputs guide decisions; do not auto-enforce
- Transparent rationales and citations for accountability
- Continuous monitoring for unintended bias and drift

Repository guide

- `backend/` FastAPI API and pipeline placeholders
- `frontend/` Research-style demo interface
- `docs/` Thesis, research plan, evaluation, changelog

Citation
Live demo

- Enable GitHub Pages: repository Settings → Pages → Source: "Deploy from a branch", Branch: `main`, Folder: `/docs`
- Then open: `https://navignareddy.github.io/SocialLens-Research-Project/`


If you use or extend SocialLens in research, please cite this repository.


