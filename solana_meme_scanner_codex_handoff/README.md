# solana-meme-launch-scanner

Local-first Python project for collecting, storing, and analyzing Solana meme launch lifecycle data.

## Milestone 1 Scope

This milestone delivers:

- Python project skeleton
- SQLite + SQLAlchemy schema and session helpers
- Typer CLI shell
- Placeholder module packages for future milestones
- Tests proving DB table creation from metadata

No external API collectors are implemented in this milestone.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
python -m pip install -e .[dev]
```

3. Copy environment template if needed:

```bash
cp .env.example .env
```

## CLI Usage

Show help:

```bash
python -m app.cli --help
```

Initialize database tables:

```bash
python -m app.cli db init
```

Inspect database status:

```bash
python -m app.cli db status
```

## Testing

```bash
python -m pytest
```

## CI Verification Fallback

If your execution environment cannot reach package indexes (for example, repeated `403 Forbidden` from pip index access), use GitHub Actions workflow `.github/workflows/milestone1-verify.yml`, which runs:

- `python -m pip install -e .[dev]`
- `python -m pytest`
- `python -m app.cli --help`
