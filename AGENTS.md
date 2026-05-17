# AGENTS.md

## Repository Mission
Build a local-first Python tool for collecting, storing, analyzing, and scanning Solana meme coin launch charts.

The product is a scanner and backtest database, not a trading bot.

Primary outcomes:
- collect historical Solana / Pump.fun-style launch data
- store token, pool, OHLCV, liquidity, and buy/sell pressure proxy data
- label launch lifecycle phases from chart data
- backtest first-dump / dead-cat-bounce setups
- scan live candidates for manual review
- support later enrichment with holder, dev, sniper, and bundler data

## Current Repository Root Rule
The actual project must live at repository root.

Do not build inside wrapper folders.

The folder `solana_meme_scanner_codex_handoff/` is a legacy bootstrap artifact from an earlier failed setup. Treat it as deprecated until it is removed. Do not add new code, tests, workflows, or docs inside it.

Expected root-level project shape:

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

## Codex Operating Rules
Before implementation work:
- read this file
- read relevant `.agents/skills/*/SKILL.md` files when available
- create or update `IMPLEMENTATION_PLAN.md`
- stop after planning when explicitly asked to plan only

During implementation:
- work one milestone at a time
- keep changes small and testable
- run relevant tests before declaring completion
- update `PROGRESS.md` with exact status, tests, blockers, and next step
- do not silently mock external APIs except in tests
- do not invent API behavior
- do not implement trading or order execution

## Milestone 1 Scope
Milestone 1 is only the project skeleton and local database foundation.

Allowed:
- Python packaging
- SQLite configuration
- SQLAlchemy models
- Typer CLI shell
- tests for table creation and basic constraints
- GitHub Actions CI
- placeholder packages for future collectors and phase logic

Not allowed in Milestone 1:
- external API calls
- live scanner logic
- wallet enrichment
- dashboards
- ML models
- trading execution

## Engineering Standards
- Python 3.11 or newer
- SQLite first
- SQLAlchemy for database models
- Typer for CLI commands
- pytest for tests
- `.env` for optional keys and local config
- no hardcoded secrets
- no required paid API keys for the MVP skeleton

## Verification Standards
A milestone is complete only when at least one reliable verification path exists.

Preferred local verification:

```bash
python -m pip install -e .[dev]
python -m pytest
python -m app.cli --help
```

If the Codex environment cannot install dependencies because of network or package-index restrictions, add a root-level GitHub Actions workflow that runs the same commands in CI and document the limitation in `PROGRESS.md`.

## Git Standards
- Use feature branches.
- Commit coherent passing states.
- Do not merge broken verification states.
- Open PRs for milestone work.
- PR summaries must include files changed, tests run, verification status, and remaining risks.
