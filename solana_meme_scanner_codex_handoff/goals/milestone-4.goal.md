# Milestone 4 Goal — Backtest v0

## Goal Command

Complete Milestone 4: implement the first dead-cat-bounce backtest strategy using stored phase labels and candles. Store results in `backtest_results`.

## Scope

Implement:

- `app/backtest/strategies.py`
- `app/backtest/runner.py`
- `app/backtest/metrics.py`
- CLI command:
  - `backtest`

## Strategy v0

Candidate:

- first ATH exists
- retrace from ATH between 40% and 70%
- volume retention during dump above threshold
- liquidity data available or not terminal
- candidate occurs within early launch window

Entry variants:

- enter when price rises 10% from dump low
- enter when green candle closes above prior candle high
- enter at fixed retrace zone if enough candles exist

Exit variants:

- take profit at +20%, +30%, +50%, +100%
- stop below dump low
- time stop after 10, 20, or 30 minutes

## Acceptance Criteria

- Backtest results are stored.
- CLI prints win rate, average return, median return, max favorable excursion, and max adverse excursion.
- Tests cover at least one winning and one losing synthetic case.
- `PROGRESS.md` is updated.
