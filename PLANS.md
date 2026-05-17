# PLANS.md

## Purpose
This repository uses executable milestone plans so Codex can work in small verified chunks.

Before implementation, Codex must create or update `IMPLEMENTATION_PLAN.md`.

## Required Plan Format

```md
# Implementation Plan — Milestone X

## Objective

## Files

## Steps
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Tests

## Acceptance Criteria

## Risks

## Progress Log
```

## Execution Rules
- Complete tasks in checklist order.
- Test after each meaningful checkpoint.
- Update `PROGRESS.md`.
- Do not skip failing tests.
- Do not mark work complete unless acceptance criteria pass.
- If blocked, stop and write the blocker clearly.

## Completion Rule
A milestone is done only when the verification commands pass in the available environment, or a CI fallback is added because local dependency installation is unavailable.
