# Inbox Agent

An email assistant I'm building to learn how agents work, both the
deterministic kind and the AI kind. It sorts new Gmail into labels, tells me
when someone I'm waiting on replies, and later drafts replies and answers
questions about my inbox. I'm building it in public, one step at a time.

## Why

Most "AI agent" tutorials start with a framework and a model choosing every
step. I want to understand what sits underneath first. So this starts with no
AI at all, adds one model call where rules run out, then builds the agent loop
by hand, and only at the end rebuilds it in LangGraph to see what the framework
does for me.

An inbox is a good place to learn this. It's real data that arrives on its own,
most of it is easy to sort with plain rules, a few messages actually need a
person, and getting it wrong is cheap as long as the agent can't send or delete
anything.

## Roadmap

- [ ] **0. Setup.** Repo, Gmail API sign-in, secret scanning, fictional test data.
- [ ] **1. No AI.** Fetch new mail and label it with plain rules. Send a
      Telegram message when a rule marks a message important, like a reply
      from someone on my waiting list. Promotions and newsletters never notify.
- [ ] **2. One AI step.** Mail the rules can't place goes to a model, which picks
      a label and decides whether it's worth a notification. Its answer is
      checked by code and scored against an answer key.
- [ ] **3. Agent loop, by hand.** Ask the inbox a question ("what came in from
      GitHub this week?") or get a draft reply. The model chooses which tools to
      call; the loop is plain Python against the API, no framework.
- [ ] **4. Guardrails.** Which actions are allowed is enforced in code, not in
      the prompt. Audit log, step and cost limits, approve or skip from Telegram.
- [ ] **5. Evals and tracing.** A growing test set, a trace for every run, a
      miss rate tracked over time.
- [ ] **6. LangGraph.** Rebuild the agent in LangGraph and compare it with the
      hand-built version.
- [ ] **7. A different inbox.** Run the same pipeline on a different kind of
      incoming message, with fictional data, to see what carries over.

## Rules

- **It never sends, deletes or unsubscribes.** It adds labels and writes
  drafts. Archiving or marking mail read may come later, only behind an
  approval step.
- **Dry run by default.** It shows what it would do until told to apply it.
- **Narrowest Gmail permissions** that allow labels and drafts.
- **No personal data in this repo.** My addresses, contacts and real emails
  live in a local config file that git ignores. The repo has an example config
  and a set of made-up emails to test against.

## Models

It uses the Anthropic API for now. Step 2 compares Claude Haiku, Sonnet and
Opus on the same answer key for accuracy and cost per email. Later it moves to
a local model running on my own machine. The model call is one function, so
switching providers is a config change.

## Status

Step 0. Nothing runs yet.

## License

MIT
