# Solana Meme Launch Scanner

Local-first research tool for collecting Solana meme coin launch data, labeling launch phases, backtesting first-dump / dead-cat-bounce setups, and scanning live candidates for manual review.

This is a scanner and backtest database. It is not a trading bot.

## Product Goal

Build a usable historical database of Solana / Pump.fun-style launches with:

- token and pool metadata
- OHLCV candles
- liquidity and volume data
- buy/sell pressure proxies where available
- launch lifecycle phase labels
- backtest results for dead-cat-bounce strategy variants
- future enrichment fields for holders, dev wallets, snipers, and bundlers

## Codex Setup

Codex should read root-level `AGENTS.md` before work.

Project-specific skills live under:

```text
.agents/skills/
```

Current skills:

```text
.agents/skills/agentic-coding-discipline/SKILL.md
.agents/skills/launch-data-model/SKILL.md
.agents/skills/api-collection/SKILL.md
.agents/skills/phase-backtest/SKILL.md
```

Do not build inside `solana_meme_scanner_codex_handoff/`. That folder is a deprecated artifact from an earlier failed bootstrap.

## Intended Root Structure

```text
AGENTS.md
README.md
pyproject.toml
pytest.ini
.env.example
.github/workflows/ci.yml
app/
tests/
.agents/skills/
```

## Milestone 1

Milestone 1 should create only the project skeleton and database foundation:

- Python packaging
- SQLite configuration
- SQLAlchemy models
- Typer CLI shell
- pytest tests for table creation and basic constraints
- root-level GitHub Actions CI
- placeholder packages for future collectors, phase logic, backtests, and scanner modules

No external API calls should be implemented in Milestone 1.

## Verification Commands

Preferred local verification:

```bash
python -m pip install -e .[dev]
python -m pytest
python -m app.cli --help
```

If local dependency installation is blocked by the Codex environment, use root-level GitHub Actions CI as the verification fallback and document the blocker in `PROGRESS.md`.

## First Codex Prompt

Use Codex Plan mode first:

```text
/plan Read AGENTS.md, README.md, and all relevant .agents/skills/*/SKILL.md files. Create IMPLEMENTATION_PLAN.md for Milestone 1 only. Do not implement code yet. The plan must identify files to create or modify, step-by-step tasks, tests to run, acceptance criteria, risks, and stop conditions. Stop after writing the plan.
```

After reviewing the plan, start implementation in a separate Codex message.
