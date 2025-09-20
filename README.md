# Inbox Agent (LangGraph)

A small, educational project to learn **agentic AI** with **LangGraph** by building an inbox assistant that can **retrieve a category of emails you ask for** and then **perform an action** (move to a label, archive, mark read, trash, attempt unsubscribe, etc.).

---

## Why this project exists

> **Intended purpose:** to learn the core concepts of agentic systems (stateful graphs, tool use, routing, retries, and human‑in‑the‑loop) using a practical, low‑risk workflow: email retrieval + optional actions.

By the end, I hope to understand:

* How to model a task as a **graph** of nodes (planner, retriever, actor, confirmer).
* How to define a **state** object and pass it between nodes.
* How to wrap external capabilities (Gmail API) as **tools** the agent can call.
* How to add **guardrails**: dry‑run mode, confirmation prompts, and least‑privilege OAuth scopes.
* How to ship a tiny CLI / API around a graph.

---

## Features (MVP)

1. **Query → Retrieve**: “Show me promotional emails from last 7 days”, “Find emails from GitHub with ‘invoice’ in the subject”, etc.
2. **Summarize or List**: Return a compact table (sender, subject, date) and counts.
3. **Action (opt‑in)**: archive, move to label, mark read, trash, or **attempt unsubscribe**.
4. **Dry‑Run by default**: prints what it *would* do. Actions require `--apply` or an explicit confirmation node.
5. **Human‑in‑the‑Loop**: the graph pauses for confirmation before mutating emails (unless `--force`).

> You can learn incrementally: start read‑only (safe), then add actions.

## Educational Checklist

* [ ] Define `AgentState` (pydantic) and ensure every node reads/writes it.
* [ ] Implement planner with a minimal ruleset; later swap for an LLM tool‑use prompt.
* [ ] Wrap Gmail search and actions as callable tools.
* [ ] Wire nodes with LangGraph `StateGraph` and conditional edges.
* [ ] Add dry‑run and confirmation.
* [ ] Ship a CLI; optionally add an API.

---

## License

MIT (or your choice). This repo is for learning purposes.
