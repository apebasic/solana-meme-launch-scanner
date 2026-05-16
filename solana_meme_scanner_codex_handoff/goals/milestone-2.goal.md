# Milestone 2 Goal — Data Collection

## Goal Command

Complete Milestone 2: implement free/public data collection for Solana meme token and pool metadata plus OHLCV candles. Use Dexscreener and GeckoTerminal first. Do not require paid API keys. Store results in the existing SQLite schema. Keep collectors modular, rate-limited, and testable.

## Scope

Implement:

- `app/collectors/dexscreener.py`
- `app/collectors/geckoterminal.py`
- `app/services/discovery_service.py`
- `app/services/ohlcv_service.py`
- CLI commands:
  - `collect-recent`
  - `collect-ohlcv`

## Acceptance Criteria

- Can collect at least a small batch of Solana token/pool metadata.
- Can store OHLCV candles for available pools.
- Duplicate inserts are avoided.
- External API failures are handled without corrupting the database.
- Tests cover parser/storage logic using fixtures.
- `PROGRESS.md` is updated.

## Stop Conditions

Stop if public API shape is uncertain and cannot be verified. Document exact uncertainty and create a minimal adapter/TODO instead of guessing.
