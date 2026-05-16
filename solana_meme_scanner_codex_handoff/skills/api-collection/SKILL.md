---
name: api-collection
description: Use when implementing free/public Solana token, pool, OHLCV, or transaction collectors for Dexscreener, GeckoTerminal, Solana RPC, Moralis, Bitquery, Birdeye, Helius, or similar APIs.
---

# API Collection Skill

## Purpose

Implement collectors that gather Solana meme launch data with minimal assumptions.

## Source Priority

1. GeckoTerminal for pool OHLCV and pool metadata.
2. Dexscreener for Solana pair/token metadata and chart links.
3. Solana RPC for transaction/signature lookups where needed.
4. Optional APIs only when keys exist in `.env`.

## Rules

- Do not hardcode keys.
- Do not require paid APIs for MVP.
- Put all API assumptions in collector docstrings.
- Store raw payloads in `metadata_json` or `raw_json` when useful.
- Add retry and timeout logic.
- Respect rate limits.
- Do not silently drop errors. Log them with token/pool context.
- Do not corrupt the database on partial API failures.

## Collector Shape

Each collector should expose narrow methods, for example:

- `fetch_pair(pair_address)`
- `search_recent_solana_pairs(...)`
- `fetch_pool_ohlcv(pool_address, timeframe, before_timestamp=None)`
- `fetch_token_metadata(mint_address)`

## Testing

- Unit test parsers with fixture JSON.
- Avoid live API tests as required test suite.
- If live smoke tests exist, mark them optional.
