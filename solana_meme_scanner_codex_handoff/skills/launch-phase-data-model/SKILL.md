---
name: launch-phase-data-model
description: Use when designing or modifying the database schema, SQLAlchemy models, launch metrics, OHLCV storage, phase labels, holder snapshots, wallet events, or backtest result tables for the Solana meme launch scanner.
---

# Launch Phase Data Model Skill

## Purpose

Design and maintain the database model for a Solana meme launch scanner and backtest system.

The database must support:

- historical token launch collection
- OHLCV candle analysis
- launch phase detection
- dead-cat-bounce backtesting
- future holder/dev/sniper/bundler enrichment

## Core Tables

Implement these tables first:

1. `tokens`
2. `pools`
3. `ohlcv_candles`
4. `launch_metrics`
5. `phase_labels`
6. `backtest_results`
7. `holder_snapshots`
8. `wallet_events`

## Table Requirements

### `tokens`

One row per token mint.

Fields:

- `id`
- `chain`
- `mint_address`
- `symbol`
- `name`
- `description`
- `created_at_detected`
- `launch_timestamp_estimated`
- `source`
- `pumpfun_url`
- `dexscreener_url`
- `geckoterminal_url`
- `first_seen_at`
- `metadata_json`
- `created_at`
- `updated_at`

Indexes:

- unique `mint_address`
- `launch_timestamp_estimated`
- `symbol`

### `pools`

One row per trading pool.

Fields:

- `id`
- `token_id`
- `pool_address`
- `dex`
- `quote_token`
- `base_token`
- `created_at_detected`
- `first_seen_at`
- `liquidity_usd_initial`
- `liquidity_usd_latest`
- `fdv_latest`
- `market_cap_latest`
- `source`
- `metadata_json`
- `created_at`
- `updated_at`

Indexes:

- unique `pool_address`
- `token_id`
- `dex`

### `ohlcv_candles`

One row per candle.

Fields:

- `id`
- `token_id`
- `pool_id`
- `timeframe`
- `timestamp`
- `open`
- `high`
- `low`
- `close`
- `volume`
- `volume_usd`
- `tx_count`
- `buy_count`
- `sell_count`
- `buy_volume`
- `sell_volume`
- `source`
- `created_at`

Indexes:

- unique `token_id`, `timeframe`, `timestamp`
- unique `pool_id`, `timeframe`, `timestamp`

### `launch_metrics`

One row per token after phase analysis.

Fields:

- `id`
- `token_id`
- `pool_id`
- `timeframe`
- `launch_time`
- `first_trade_time`
- `first_ath_time`
- `first_ath_price`
- `first_ath_market_cap`
- `first_ath_volume_window`
- `time_to_first_ath_minutes`
- `pump_return_from_launch`
- `max_slope_pre_ath`
- `green_candle_ratio_pre_ath`
- `volume_expansion_ratio_pre_ath`
- `first_dump_low_time`
- `first_dump_low_price`
- `retrace_from_ath_pct`
- `time_from_ath_to_dump_low_minutes`
- `dump_speed_pct_per_min`
- `red_candle_ratio_dump`
- `volume_retention_dump`
- `first_bounce_start_time`
- `first_bounce_high_time`
- `first_bounce_high_price`
- `bounce_from_dump_low_pct`
- `bounce_reclaim_of_ath_loss_pct`
- `time_to_bounce_minutes`
- `bounce_volume_ratio`
- `second_ath_made_boolean`
- `second_ath_time`
- `second_ath_price`
- `max_price_after_bounce`
- `max_return_after_bounce`
- `died_after_first_dump_boolean`
- `terminal_liquidity_loss_boolean`
- `analysis_status`
- `analysis_notes`
- `created_at`
- `updated_at`

Indexes:

- unique `token_id`
- `first_ath_time`
- `retrace_from_ath_pct`
- `bounce_from_dump_low_pct`

### `phase_labels`

Stores algorithmic lifecycle labels.

Fields:

- `id`
- `token_id`
- `pool_id`
- `timeframe`
- `phase_name`
- `start_time`
- `end_time`
- `start_price`
- `end_price`
- `high_price`
- `low_price`
- `volume_sum`
- `confidence_score`
- `method_version`
- `metadata_json`
- `created_at`

Allowed `phase_name` values:

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

### `backtest_results`

One row per token per strategy version.

Fields:

- `id`
- `token_id`
- `strategy_name`
- `strategy_version`
- `candidate_time`
- `entry_price`
- `entry_time`
- `exit_price`
- `exit_time`
- `stop_price`
- `take_profit_price`
- `max_favorable_excursion_pct`
- `max_adverse_excursion_pct`
- `result_pct`
- `win_boolean`
- `reason_entered`
- `reason_exited`
- `metadata_json`
- `created_at`

Indexes:

- `strategy_name`, `strategy_version`
- `token_id`

### `holder_snapshots`

Future enrichment table. Create schema but do not require it for MVP.

Fields:

- `id`
- `token_id`
- `snapshot_time`
- `holder_count`
- `top_10_supply_pct`
- `top_20_supply_pct`
- `top_50_supply_pct`
- `dev_supply_pct`
- `bundle_supply_pct`
- `sniper_supply_pct`
- `insider_supply_pct`
- `source`
- `raw_json`
- `created_at`

Indexes:

- `token_id`, `snapshot_time`

### `wallet_events`

Future enrichment table.

Fields:

- `id`
- `token_id`
- `wallet_address`
- `event_time`
- `event_type`
- `amount_token`
- `amount_sol`
- `amount_usd`
- `supply_pct`
- `is_dev`
- `is_sniper`
- `is_bundle`
- `is_top_holder`
- `source`
- `tx_signature`
- `raw_json`
- `created_at`

Indexes:

- `token_id`, `wallet_address`
- `token_id`, `event_time`
- `tx_signature`

## Modeling Rules

- `tokens` are keyed by mint address.
- `pools` are keyed by pool address.
- `ohlcv_candles` must be unique by `pool_id`, `timeframe`, and `timestamp`.
- Holder and wallet tables are future enrichment tables. Create them, but do not require them for MVP workflows.
- Use JSON fields only for raw API payloads or metadata that does not deserve first-class columns yet.
- Do not store strategy-specific metrics only in generic JSON if they will be queried often.

## Validation

After model changes:

1. create the database from scratch
2. verify all tables exist
3. insert a small token/pool/candle fixture
4. query it back
5. run tests

## Do Not Do

- Do not implement trading.
- Do not overfit to one API response shape.
- Do not require holder data before chart data works.
- Do not use CSV as the primary database.
