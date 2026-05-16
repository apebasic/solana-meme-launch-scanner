---
name: phase-detection-backtest
description: Use when implementing launch phase detection, first ATH detection, first dump detection, dead-cat-bounce detection, scanner scoring, or backtest logic.
---

# Phase Detection And Backtest Skill

## Purpose

Classify early meme launch lifecycle phases from OHLCV candles and test dead-cat-bounce strategies.

## Core Lifecycle

Classify:

1. `launch`
2. `first_pump`
3. `first_ath`
4. `first_dump`
5. `dead_cat_bounce`
6. `post_bounce_dump`
7. `second_leg`
8. `accumulation`
9. `death`
10. `unknown`

## MVP Detection Rules

Use simple rules first.

### First ATH

- Identify first major local high before a retrace.
- Default retrace threshold: 35%.
- Store time, price, return from launch, and volume window.

### First Dump

- Begins after first ATH.
- Default condition: retrace at least 35% from first ATH.
- Search window default: within 120 minutes after ATH.
- Store dump low, speed, volume retention, and red candle ratio.

### Dead-Cat Bounce

- First meaningful rebound after dump low.
- Default condition: price rises at least 20% from dump low.
- Store bounce high, time to bounce, and volume ratio.

### Death

Mark as likely death if:

- no meaningful bounce within the max window
- price remains near or below dump low
- volume collapses
- liquidity collapses if liquidity data is available

## Backtest v0

Candidate condition:

- first ATH exists
- retrace from ATH between 40% and 70%
- volume retention during dump above threshold
- candidate occurs within early launch window

Entry variants:

- price rises 10% from dump low
- green candle closes above prior candle high
- fixed retrace-zone entry

Exit variants:

- take profit at +20%, +30%, +50%, +100%
- stop below dump low
- time stop after 10, 20, or 30 minutes

## Rules

- Do not overfit.
- Make thresholds configurable.
- Store method version with labels/results.
- Synthetic tests are mandatory.
- Prefer explainable metrics over ML.
