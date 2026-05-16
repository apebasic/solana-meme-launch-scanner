# Milestone 3 Goal — Phase Detection Engine

## Goal Command

Complete Milestone 3: implement rule-based phase detection from stored OHLCV candles. Detect first ATH, first dump, dead-cat bounce, continuation, and death/unknown states. Populate `launch_metrics` and `phase_labels`.

## Scope

Implement:

- `app/phase_engine/metrics.py`
- `app/phase_engine/detector.py`
- `app/phase_engine/labels.py`
- CLI command:
  - `analyze-phases`

## Acceptance Criteria

- Given stored candles, the engine creates launch metrics.
- Given stored candles, the engine creates phase labels.
- Tests cover synthetic examples:
  - pump then dump then bounce
  - pump then death
  - insufficient data
- `PROGRESS.md` is updated.
