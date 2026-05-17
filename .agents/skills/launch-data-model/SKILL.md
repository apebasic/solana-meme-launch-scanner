---
name: launch-data-model
description: Use when designing or changing database models, migrations, SQLite storage, SQLAlchemy tables, OHLCV candles, token/pool schemas, launch metrics, phase labels, holder snapshots, wallet events, or backtest result tables for the Solana launch scanner.
---

# Launch Data Model Skill

## Purpose
Maintain the database model for a local-first Solana meme launch scanner and backtest system.

The database must support:
- historical token launch collection
- pool and OHLCV candle storage
- launch lifecycle phase labeling
- first-dump / dead-cat-bounce backtesting
- later enrichment with holder, dev, sniper, and bundler data

## First Principles
- Store raw market data before building strategy logic.
- Keep chart data and wallet enrichment separate.
- Do not block the MVP on wallet intelligence.
- Prefer explicit queryable columns for metrics used in filtering or backtesting.
- Use JSON only for raw API payloads or metadata that is not yet stable.

## Required Core Tables
Milestone 1 should include these tables:

1. `tokens`
2. `pools`
3. `ohlcv_candles`
4. `launch_metrics`
5. `phase_labels`
6. `backtest_results`
7. `holder_snapshots`
8. `wallet_events`

## Modeling Rules
- `tokens` are keyed by Solana mint address.
- `pools` are keyed by pool address.
- A token can have multiple pools.
- A pool belongs to one base token for this project’s analysis scope.
- `ohlcv_candles` must support multiple timeframes.
- `ohlcv_candles` must avoid duplicate candles.
- `holder_snapshots` and `wallet_events` are future enrichment tables; create them early, but do not require data in them for Milestone 1.
- Backtest results must be linked to a strategy name and strategy version.

## Minimum Uniqueness / Index Requirements
Implement equivalent SQLAlchemy constraints or indexes for:
- unique `tokens.mint_address`
- unique `pools.pool_address`
- unique candle identity by `token_id`, `timeframe`, `timestamp`
- unique candle identity by `pool_id`, `timeframe`, `timestamp`
- indexed `phase_labels(token_id, timeframe, phase_name)`
- indexed `backtest_results(strategy_name, strategy_version)`

## Phase Names
Use a constrained set of names where practical:
- `launch`
- `first_pump`
- `first_ath`
- `first_dump`
- `dead_cat_bounce`
- `post_bounce_dump`
- `second_leg`
- `accumulation`
- `death`
- `unknown`

## Validation Checklist
After data model changes:
1. create a fresh SQLite database
2. confirm all required tables exist
3. inspect required indexes and unique constraints
4. insert a minimal token / pool / candle fixture in tests
5. run `python -m pytest`

## Do Not Do
- Do not implement external API collectors in this skill.
- Do not implement trading execution.
- Do not use CSV as the primary database.
- Do not design around one API’s response shape only.
