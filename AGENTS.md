# AGENTS.md

## Mission
Build a local-first Python tool for collecting, storing, analyzing, and scanning Solana meme coin launch charts.

Primary outcomes:
1. Historical launch database for Solana / Pump.fun-style launches.
2. OHLCV + liquidity + buy/sell-pressure proxy storage.
3. Rule-based phase labeling: launch, first pump, first ATH, first dump, dead-cat bounce, second leg, death.
4. Backtest database for first-dump / dead-cat-bounce strategies.
5. Live scanner for candidates, not an execution bot.

## Codex Operating Rules
- Work one milestone at a time.
- Before coding, read `PLANS.md`, the active `goals/*.goal.md`, and relevant `skills/*/SKILL.md` files.
- Create or update `IMPLEMENTATION_PLAN.md` before implementation.
- Do not implement trading or order execution.
- Do not invent external API behavior. If uncertain, isolate it behind an adapter and document the uncertainty.
- Do not block Milestone 1 on external APIs.
- Keep the repo root clean. The actual project must live at repository root, not inside a wrapper folder.

## Engineering Rules
- Python 3.11+.
- SQLite first.
- SQLAlchemy for models.
- Typer for CLI.
- `.env` for optional API keys.
- Small modules, testable functions, explicit acceptance checks.

## Validation Discipline
After each checkpoint:
- run relevant tests or smoke checks
- fix failures
- update `PROGRESS.md`

Milestone completion requires:
- code committed
- tests passing, or CI workflow added when local package installation is unavailable
- CLI smoke command working in a verified environment
- `PROGRESS.md` updated with exact status

## Git Discipline
- Use feature branches.
- Open PRs for milestone work.
- Do not merge broken verification states.
