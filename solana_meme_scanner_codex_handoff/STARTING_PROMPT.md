# Starting Prompt For Codex Cloud

Read this entire prompt and the repository files before coding.

You are working on a new GitHub repository for a project named:

`solana-meme-launch-scanner`

## Objective

Build a local-first Python tool that collects historical Solana meme coin launch data, stores it in SQLite, classifies launch chart phases, backtests dead-cat-bounce setups, and eventually scans live candidates.

This is not a trading bot. Do not implement order execution.

## Required First Step

Start in planning mode.

Read these files first:

- `AGENTS.md`
- `PLANS.md`
- `goals/milestone-1.goal.md`
- `skills/launch-phase-data-model/SKILL.md`

Then create:

- `IMPLEMENTATION_PLAN.md`

Do not code until the plan exists.

## Milestone To Execute

Complete Milestone 1 only.

Milestone 1 means:

- create project skeleton
- create SQLite database layer
- create SQLAlchemy models
- create Typer CLI shell
- create `.env.example`
- create README
- create tests proving database table creation works

Do not implement external API calls yet.

## Required Database Tables

Create SQLAlchemy models for:

1. `tokens`
2. `pools`
3. `ohlcv_candles`
4. `launch_metrics`
5. `phase_labels`
6. `backtest_results`
7. `holder_snapshots`
8. `wallet_events`

Use the schema in:

- `skills/launch-phase-data-model/SKILL.md`
- `goals/milestone-1.goal.md`

## Required Validation

Run:

```bash
python -m pytest
python -m app.cli --help
```

If you choose a different valid CLI invocation, document it clearly in README and `PROGRESS.md`.

## Workflow Rules

- Work only on Milestone 1.
- Keep the implementation narrow and runnable.
- Do not invent external API behavior.
- Do not add fake data except test fixtures.
- Update `PROGRESS.md` after meaningful checkpoints.
- Stop and report blockers if dependencies, tests, or schema creation fail.

## Completion

Milestone 1 is complete only if:

- tests pass
- CLI help works
- database tables can be created from SQLAlchemy metadata
- README explains setup
- `.env.example` exists
- `PROGRESS.md` records what was completed and what remains
