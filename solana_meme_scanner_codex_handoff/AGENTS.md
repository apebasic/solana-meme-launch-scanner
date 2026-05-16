# AGENTS.md

## Mission

Build a local-first Python tool for collecting, storing, analyzing, and scanning Solana meme coin launch charts.

The tool has two jobs:

1. Build a historical launch database.
2. Detect live candidates entering first-dump / dead-cat-bounce conditions.

This is a scanner and backtest database. It is not a trading bot. Do not implement order execution.

## Product Outcome

The repository should eventually produce:

- a structured SQLite database of Solana meme launches
- token and pool metadata
- OHLCV candle storage
- launch, pump, dump, bounce, death, and continuation labels
- backtest results for dead-cat-bounce strategies
- a terminal scanner for current candidates
- future-ready tables for holder, dev, sniper, and bundler enrichment

## Engineering Rules

- Use Python.
- Use SQLite first.
- Use SQLAlchemy for models.
- Use Typer for CLI unless there is a clear reason not to.
- Prefer `uv` for environment management if available.
- Keep modules small and testable.
- Do not hardcode API keys.
- Use `.env` for optional API keys.
- Public/free APIs must work without paid keys where possible.
- Optional paid/free-tier APIs may be scaffolded but must not block the MVP.

## Anti-Drift Rules

- Work one milestone at a time.
- Before coding, create or update `IMPLEMENTATION_PLAN.md`.
- Do not jump ahead to live trading, ML, dashboards, or wallet intelligence before the core database works.
- Do not invent fake APIs.
- Do not silently mock external data except in tests.
- If an API assumption is uncertain, write a small adapter with clear TODOs and document the uncertainty.
- Prefer a working narrow slice over broad unfinished architecture.

## Required Validation

After each meaningful checkpoint:

- run relevant tests
- run CLI smoke tests where applicable
- update `PROGRESS.md`
- record any blocker clearly
- do not mark a milestone complete unless acceptance criteria pass

## Files To Read Before Coding

Always read:

- `PLANS.md`
- the active file in `goals/`
- relevant files in `skills/*/SKILL.md`

## Git Discipline

- Work on a feature branch.
- Commit only coherent passing states.
- Use concise commit messages:
  - `milestone-1: create database schema`
  - `milestone-2: add geckoterminal collector`
  - `milestone-3: implement phase detector`

## Definition of Done

A task is done only when:

- code exists
- tests pass
- CLI command works where applicable
- database or output artifact can be inspected
- `PROGRESS.md` says what changed and what remains
