# rag_to_riches

A from-the-basics **Retrieval-Augmented Generation (RAG)** project in Python, built to understand each moving part (chunking, embeddings, similarity search, generation) before reaching for a framework. Uses local models through [Ollama](https://ollama.com).

> **Status: work in progress.** The dataset loader and similarity maths are done; the embedding store and the generation step are next. See the roadmap below.

## How RAG works here

```
documents ─► chunks ─► embeddings (Ollama) ─► vector store
                                                  │
query ─► query embedding ─► cosine similarity ────┘
                                  │
                       top-k chunks + question ─► LLM ─► answer
```

## What exists today

| File | Purpose |
| --- | --- |
| `load_dataset.py` | Loads `data/cat-facts.txt` (149 short facts) into memory |
| `retrieval.py` | `cosine_similarity(a, b)` with NumPy, safe against zero vectors |
| `vector_db.py` | Embedding store (in progress) |
| `main.py` | Entry point that embeds the dataset into the store |

## Roadmap

- [x] Dataset loader
- [x] Cosine similarity
- [ ] Embed chunks with an Ollama embedding model and keep them in an in-memory store
- [ ] Top-k retrieval for a query
- [ ] Prompt assembly and answer generation with a local chat model
- [ ] Simple retrieval evaluation (hit rate on a labelled question set)

## Setup

Requires Python 3.14+, [uv](https://docs.astral.sh/uv/) and a running Ollama server.

```sh
uv sync
ollama pull nomic-embed-text   # embedding model (example)
uv run python main.py
```

## Why this exists

To learn RAG by writing it myself. A fuller, evaluated application of the same ideas lives in [helpdesk-agent](https://github.com/HimSlayer001/helpdesk-agent).
