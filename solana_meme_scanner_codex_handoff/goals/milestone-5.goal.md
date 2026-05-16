# Milestone 5 Goal — Live Scanner MVP

## Goal Command

Complete Milestone 5: implement a live scanner that fetches recent Solana pairs, applies the phase detection/scoring logic, and prints ranked candidates for manual review.

## Scope

Implement:

- `app/scanner/live_scanner.py`
- `app/scanner/scoring.py`
- CLI command:
  - `scan-live`

## Candidate States

- `FIRST_PUMP_ACTIVE`
- `FIRST_DUMP_ACTIVE`
- `BOUNCE_SETUP`
- `BOUNCE_STARTED`
- `AVOID_DEATH`
- `UNKNOWN`

## Output Columns

- token symbol
- mint address
- pool address
- age
- current price
- first ATH price
- retrace from ATH
- dump low
- bounce from low
- volume retention
- liquidity
- phase label
- candidate score
- chart link

## Acceptance Criteria

- CLI prints a ranked terminal table.
- Scanner does not trade.
- API failures are handled gracefully.
- Scoring rules are transparent and configurable.
- `PROGRESS.md` is updated.
