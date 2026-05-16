# Milestone 1 Goal — Project Skeleton + Database

## Goal Command

Complete Milestone 1 for the Solana meme launch scanner: create the Python project skeleton, SQLite database layer, SQLAlchemy models, Typer CLI shell, `.env.example`, README, and tests proving database table creation works. Verify success by running the test suite and CLI help command. Work only on Milestone 1. Do not implement external API calls yet. Update `PROGRESS.md` after each checkpoint. Stop and report blockers if dependencies cannot install, tests cannot run, or the schema cannot be created cleanly.

## Scope

Create:

- `pyproject.toml`
- `README.md`
- `.env.example`
- `AGENTS.md` if missing
- `PROGRESS.md`
- `app/__init__.py`
- `app/config.py`
- `app/cli.py`
- `app/database/models.py`
- `app/database/session.py`
- `app/database/__init__.py`
- placeholder packages for collectors, services, phase_engine, backtest, scanner, exports, utils
- `tests/test_database.py`

## Required Database Tables

- `tokens`
- `pools`
- `ohlcv_candles`
- `launch_metrics`
- `phase_labels`
- `backtest_results`
- `holder_snapshots`
- `wallet_events`

## Acceptance Criteria

Milestone 1 is complete only if:

- project installs locally
- database tables can be created from SQLAlchemy metadata
- tests pass
- CLI help works
- README explains setup
- `.env.example` contains optional API key placeholders
- no external API calls are implemented
- `PROGRESS.md` records completed work and next milestone

## Verification Commands

Run:

```bash
python -m pytest
python -m app.cli --help
```

If the project uses another valid CLI invocation, document it in README and `PROGRESS.md`.

## Stop Conditions

Stop and report clearly if:

- dependency resolution fails
- tests cannot run
- SQLAlchemy model creation fails
- project structure conflicts with existing files
- implementation would require external API access before Milestone 2
