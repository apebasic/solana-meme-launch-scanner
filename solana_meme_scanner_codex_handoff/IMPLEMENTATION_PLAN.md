# Implementation Plan — Milestone 1

## Objective

Deliver Milestone 1 only: establish a runnable Python project skeleton with a SQLite/SQLAlchemy data layer, required database schema tables, a Typer CLI shell, baseline project docs/config, and tests that verify schema creation (without implementing any external API collection logic).

## Files

### Files to create

- `pyproject.toml`
- `README.md`
- `.env.example`
- `app/__init__.py`
- `app/config.py`
- `app/cli.py`
- `app/database/__init__.py`
- `app/database/session.py`
- `app/database/models.py`
- `app/collectors/__init__.py`
- `app/services/__init__.py`
- `app/phase_engine/__init__.py`
- `app/backtest/__init__.py`
- `app/scanner/__init__.py`
- `app/exports/__init__.py`
- `app/utils/__init__.py`
- `tests/test_database.py`

### Files to modify

- `PROGRESS.md` (checkpoint updates and milestone status)

## Steps

- [ ] **Step 1 — Baseline project scaffolding**
  - Create package structure under `app/` and `tests/`.
  - Add `pyproject.toml` with core dependencies for Milestone 1 (SQLAlchemy, Typer, pytest, dotenv/config support as needed).
  - Ensure module import paths are consistent with `python -m app.cli` invocation.

- [ ] **Step 2 — Configuration and database session layer**
  - Implement `app/config.py` for local-first configuration (SQLite path, optional env var loading).
  - Implement `app/database/session.py` with SQLAlchemy engine/session setup and metadata bootstrap helper.
  - Keep DB initialization deterministic and test-friendly.

- [ ] **Step 3 — Implement SQLAlchemy schema models**
  - Implement all required tables in `app/database/models.py`:
    - `tokens`, `pools`, `ohlcv_candles`, `launch_metrics`, `phase_labels`, `backtest_results`, `holder_snapshots`, `wallet_events`
  - Add required uniqueness constraints and indexes from `goals/milestone-1.goal.md` and `skills/launch-phase-data-model/SKILL.md`.
  - Include relationships only where they improve clarity for Milestone 1 and do not overcomplicate schema bootstrap.

- [ ] **Step 4 — CLI shell (no collectors yet)**
  - Implement `app/cli.py` Typer app with help output and at least one safe command (e.g., schema init/check command) appropriate to Milestone 1.
  - Ensure CLI does not perform external API calls.

- [ ] **Step 5 — Documentation and environment template**
  - Create `README.md` with setup, local run instructions, and Milestone 1 limitations.
  - Create `.env.example` with optional placeholder API keys/values (non-required for Milestone 1 execution).
  - Document canonical verification commands.

- [ ] **Step 6 — Tests for schema creation**
  - Implement `tests/test_database.py` to verify metadata creates all required tables in SQLite.
  - Include assertions for table presence and minimal structural sanity checks (e.g., key unique constraints/index presence where straightforward to assert).
  - Avoid network, API, or integration dependencies.

- [ ] **Step 7 — Validation and progress reporting**
  - Run required verification commands.
  - Update `PROGRESS.md` with completed Milestone 1 scope, verification outcomes, and next milestone handoff.

## Tests

Planned verification commands for Milestone 1:

- `python -m pytest`
- `python -m app.cli --help`

Optional additional smoke checks (if implemented in CLI):

- `python -m app.cli db init`
- `python -m app.cli db status`

## Acceptance Criteria

Milestone 1 is accepted only when all are true:

1. Project skeleton and package layout exist per milestone scope.
2. SQLAlchemy metadata can create all 8 required tables in SQLite cleanly.
3. Required constraints/indexes are implemented for core query and uniqueness guarantees.
4. Test suite passes via `python -m pytest`.
5. CLI help works via `python -m app.cli --help`.
6. `README.md` documents setup and Milestone 1 usage.
7. `.env.example` exists with optional placeholders.
8. No external API calls are implemented.
9. `PROGRESS.md` records what was completed and what remains.

## Risks

- **Dependency drift risk:** Typer/SQLAlchemy/pytest version mismatches may break startup or tests.
- **SQLite compatibility risk:** certain column types/defaults may behave differently across SQLite versions.
- **Schema interpretation risk:** ambiguity in whether all indexes/constraints should be asserted in tests vs. implemented only in models.
- **Over-scope risk:** adding collector logic prematurely would violate milestone boundaries.

## Recovery Notes

- If dependency setup fails, pin compatible versions in `pyproject.toml` and document rationale.
- If schema creation fails, isolate table/model causing metadata error and validate incrementally.
- If CLI import/run fails, verify package/module layout and `python -m` entrypoint assumptions.
- If tests are flaky due to filesystem DB paths, switch tests to temporary SQLite files or in-memory DB fixtures.

## Checklist

- [ ] Read and align with `AGENTS.md`, `PLANS.md`, milestone goal, and relevant skill file.
- [ ] Create project skeleton and packaging files.
- [ ] Implement config and DB session layer.
- [ ] Implement all required SQLAlchemy models/tables.
- [ ] Implement Typer CLI shell and help path.
- [ ] Add `.env.example` and `README.md`.
- [ ] Add database creation tests.
- [ ] Run `python -m pytest`.
- [ ] Run `python -m app.cli --help`.
- [ ] Update `PROGRESS.md` with checkpoint and milestone status.
