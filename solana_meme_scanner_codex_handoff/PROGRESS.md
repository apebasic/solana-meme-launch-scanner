# PROGRESS.md

## Current Status

Milestone 1 implementation is complete. Local verification is blocked by environment package index access; GitHub Actions verification workflow has been added to execute milestone checks in CI.

## Active Milestone

Milestone 1 — Project Skeleton + Database

## Log

- 2026-05-17 Checkpoint 1: Inspected packaging and environment (`python --version`, `pip --version`, `pip config`, `pip debug`) and confirmed dependency-install failure during build dependency resolution.
- 2026-05-17 Checkpoint 2: Simplified packaging by removing strict build-system pinning path and migrating project metadata to `setup.py`; moved pytest config to `pytest.ini`.
- 2026-05-17 Checkpoint 3: Re-ran install path and confirmed blocker persists (`403 Forbidden` for package-index requests to resolve `setuptools>=40.8.0` build dependency in isolated build step).
- 2026-05-17 Checkpoint 4: Added GitHub Actions workflow `.github/workflows/milestone1-verify.yml` to run required milestone verification commands in CI.
- 2026-05-17 Checkpoint 5: Updated README with CI fallback verification instructions.

## Root Cause

The Codex runtime cannot access the configured Python package index endpoints (tunneled requests return `403 Forbidden`), which prevents pip from creating isolated build environments for editable install (`python -m pip install -e .[dev]`) because setuptools build dependency resolution cannot complete.

## Fix Applied

- Removed strict build-system pinning from `pyproject.toml` path and switched to `setup.py` + `pytest.ini` for simpler packaging metadata.
- Added `.github/workflows/milestone1-verify.yml` to run required milestone commands in an environment with package-index access.
- Documented CI fallback in README.

## Final Verification Results

Local Codex runtime:
- `python -m pip install -e .[dev]` ❌ fails with package-index `403 Forbidden` while resolving build dependency.
- `python -m pytest` ❌ blocked because dependencies were not installed.
- `python -m app.cli --help` ❌ blocked because dependencies were not installed.

CI path:
- `.github/workflows/milestone1-verify.yml` added to run required milestone verification commands remotely.

## Remaining Work

- Confirm green run of `milestone1-verify` GitHub Actions workflow.
- Do not proceed to Milestone 2 until CI verification is green.
