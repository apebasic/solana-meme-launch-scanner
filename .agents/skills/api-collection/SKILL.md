---
name: api-collection
description: Use when designing or implementing collectors, API clients, HTTP adapters, rate limiting, raw response storage, token/pool discovery, OHLCV ingestion, Solana RPC retrieval, or optional provider integrations for the Solana launch scanner.
---

# API Collection Skill

## Purpose
Implement market-data and on-chain-data collection without inventing API behavior.

This skill governs collectors for:
- Dexscreener
- GeckoTerminal
- Solana RPC
- optional providers such as Helius, Moralis, Bitquery, Birdeye, or Nansen

## Core Rule
Collectors must be adapter-based and evidence-driven.

Do not assume an endpoint, response field, rate limit, or historical coverage exists unless it is verified by current documentation, a real smoke call, or a checked fixture.

## Source Roles

### Dexscreener
Use for token and pair metadata where available:
- latest token profiles / boosts / paid orders
- pair lookup by chain and pair address
- token-to-pool/pair lookup
- multiple token address lookup
- liquidity, volume, tx count, FDV, market cap, and pair creation metadata when present in responses

Do not assume Dexscreener provides complete historical OHLCV for backtesting. Treat it primarily as discovery and metadata unless a verified endpoint proves otherwise.

### GeckoTerminal
Use for DEX market data and OHLCV ingestion when available.

Before implementation, verify the current endpoint shape and parameters against official GeckoTerminal API docs or by a smoke call. Store raw responses during early development so parser assumptions remain auditable.

### Solana RPC
Use for on-chain transaction retrieval and future enrichment.

Likely RPC methods:
- `getSignaturesForAddress` for signatures involving an address
- `getTransaction` for transaction details

Solana RPC should not be used as the first source for large-scale historical chart OHLCV unless no API source is sufficient. It is more useful for wallet/dev/sniper/bundler enrichment after the chart dataset exists.

### Optional Providers
Optional providers may be scaffolded behind interfaces but must not block the MVP:
- Helius
- Moralis
- Bitquery
- Birdeye
- Nansen

A provider requiring an API key must fail gracefully with a clear message if the key is missing.

## Collector Design Rules
- One collector module per provider.
- Keep HTTP calls separate from parsing.
- Keep parsing separate from database writes.
- Return typed normalized records from services when practical.
- Store raw JSON in metadata/raw fields during early implementation.
- Implement retries and rate limiting conservatively.
- Avoid silent data loss: log skipped records and parse failures.
- Never hardcode API keys.
- Use `.env` for optional keys.

## Minimum Collector Files
Expected future modules:

```text
app/collectors/dexscreener.py
app/collectors/geckoterminal.py
app/collectors/solana_rpc.py
app/services/discovery_service.py
app/services/ohlcv_service.py
```

## Milestone Discipline

### Milestone 1
Do not implement external API calls.

Allowed:
- placeholder collector packages
- config placeholders
- dependency planning

### Milestone 2
Implement the first real collection slice:
- token/pair discovery
- pool metadata ingestion
- OHLCV ingestion for known pools
- raw response storage where useful
- no wallet enrichment yet

## Verification Checklist
For each provider implementation:
1. cite or document the current official endpoint source in code comments or docs
2. add a small parser fixture test
3. run one smoke command when network access is available
4. store normalized output in database tables
5. update `PROGRESS.md` with endpoints used and limitations

## Do Not Do
- Do not invent Pump.fun historical endpoints.
- Do not pretend metadata snapshots are historical OHLCV.
- Do not require paid APIs for the first working version.
- Do not mix live scanner logic into collectors.
- Do not mix wallet enrichment into OHLCV ingestion.
- Do not silently continue when an API response shape changes.
