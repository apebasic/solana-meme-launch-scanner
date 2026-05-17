---
name: phase-backtest
description: Use when designing or implementing launch phase detection, chart lifecycle labeling, first ATH / first dump / dead-cat-bounce rules, scanner scoring, or backtest logic for Solana meme launch charts.
---

# Phase Backtest Skill

## Purpose
Implement rule-based chart phase detection and backtesting for Solana meme coin launches.

This project is trying to study a repeatable launch lifecycle:
- launch
- first pump
- first ATH
- first dump
- dead-cat bounce
- post-bounce dump
- possible second leg
- death / oblivion

The goal is to build a dataset and scanner, not to execute trades.

## Core Rule
Use transparent, testable rules before ML.

Do not build predictive models until the historical database, phase labels, and baseline backtests exist.

## Input Data
Phase detection should primarily consume normalized OHLCV candles:
- timestamp
- open
- high
- low
- close
- volume
- optional volume_usd
- optional tx_count
- optional buy_count / sell_count
- optional buy_volume / sell_volume

If actual buy/sell data is unavailable, use candle-based proxies only when clearly labeled as proxies.

## Phase Label Definitions

### `launch`
Early candles after first valid trading activity.

Minimum evidence:
- first non-zero volume candle
- first valid price
- pool/token metadata linked to candle series

### `first_pump`
Initial price expansion after launch.

Typical evidence:
- rising price from launch baseline
- expanding volume
- higher highs
- strong green candle ratio

### `first_ath`
The first major local high before a meaningful drawdown.

Default detection concept:
- track rolling maximum high
- first ATH candidate is confirmed after price retraces by a configurable threshold from that high
- default confirmation retrace: 35%

### `first_dump`
The first meaningful drawdown after first ATH.

Default evidence:
- retrace from first ATH >= 35%
- occurs within the early launch window
- volume has not fully disappeared

### `dead_cat_bounce`
First meaningful rebound after the first dump low.

Default evidence:
- price rebounds from dump low by configurable threshold
- default minimum rebound: 20%
- occurs before terminal volume/liquidity collapse

### `death`
Post-launch collapse where useful bounce conditions disappear.

Default evidence may include:
- no rebound above threshold within max window
- severe volume decay
- price stays near or below dump low
- liquidity collapse when liquidity data exists

## Default Parameters
Keep these configurable, not hardcoded deep inside logic:

```text
first_ath_confirm_retrace_pct = 35
first_dump_min_retrace_pct = 35
bounce_min_rebound_pct = 20
max_minutes_after_ath_for_dump = 120
max_minutes_after_ath_for_bounce = 180
min_candles_required = 30
```

## Backtest v0
First strategy family:

`first_dump_bounce_v0`

Candidate requirements:
- first ATH detected
- current/recent retrace from ATH between configurable bounds
- default band: 40% to 70%
- enough post-ATH volume remains to avoid dead/noise charts
- no confirmed terminal death condition before entry

Entry variants to test:
- enter when price rises 10% from dump low
- enter after first green candle close above prior candle high
- enter at fixed retrace band from ATH

Exit variants to test:
- take profit at +20%, +30%, +50%, +100%
- stop below dump low
- time stop after 10, 20, or 30 minutes

Store per-run metrics:
- candidate_time
- entry_time / entry_price
- exit_time / exit_price
- stop_price
- take_profit_price
- max_favorable_excursion_pct
- max_adverse_excursion_pct
- result_pct
- win_boolean
- reason_entered
- reason_exited

## Scanner Boundaries
Scanner logic should classify candidate state. It should not trade.

Allowed scanner states:
- `FIRST_PUMP_ACTIVE`
- `FIRST_DUMP_ACTIVE`
- `BOUNCE_SETUP`
- `BOUNCE_STARTED`
- `AVOID_DEATH`
- `UNKNOWN`

Scanner output should be a ranked table for manual review.

## Design Rules
- Keep pure phase logic independent from API collectors.
- Keep pure phase logic independently testable from database IO.
- Use deterministic rule versions.
- Store `method_version` or `strategy_version` for labels and backtests.
- Prefer simple functions for metric calculations.
- Do not introduce ML, notebooks, or dashboards before v0 backtest works.

## Validation Checklist
For phase/backtest changes:
1. create small synthetic OHLCV fixtures
2. test first ATH detection
3. test first dump detection
4. test bounce detection
5. test death/no-bounce case
6. test backtest result persistence or result object generation
7. run `python -m pytest`

## Do Not Do
- Do not implement trading execution.
- Do not overfit parameters to one chart screenshot.
- Do not hide rule thresholds inside undocumented constants.
- Do not mix holder/dev/sniper enrichment into phase detection v0.
- Do not claim strategy edge before backtest results exist.
