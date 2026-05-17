---
name: agentic-coding-discipline
description: Use for non-trivial coding work, debugging, refactoring, implementation planning, PR review, or any task where Codex might over-assume, over-engineer, make broad edits, or claim completion without verification.
---

# Agentic Coding Discipline Skill

## Purpose
Reduce common AI coding-agent failures:
- wrong assumptions
- hidden confusion
- missing tradeoffs
- bloated abstractions
- unrelated edits
- unverified completion claims

This skill applies to implementation discipline. Pair it with domain skills such as `launch-data-model` when working on project-specific code.

## 1. Think Before Coding
Do not silently choose an interpretation when the task is ambiguous.

Before implementing:
- state material assumptions in `IMPLEMENTATION_PLAN.md`
- surface tradeoffs when there are multiple reasonable approaches
- push back when a simpler approach would satisfy the milestone
- stop and document a blocker when requirements or dependencies are genuinely unclear

For this repository, prefer stopping over inventing API behavior or building inside the wrong directory.

## 2. Simplicity First
Implement the minimum code that satisfies the current milestone.

Rules:
- no features beyond the active milestone
- no abstractions for single-use code
- no speculative flexibility
- no dashboards, ML, live trading, or wallet intelligence during Milestone 1
- if a solution becomes much larger than needed, simplify before continuing

Senior-engineer test: if the diff looks broader than the user’s requested outcome, reduce scope.

## 3. Surgical Changes
Touch only files required by the current task.

When editing:
- do not refactor unrelated code
- do not reformat unrelated files
- do not change comments or code you do not understand
- match existing project style where it exists
- remove only unused code created by your own changes
- mention unrelated dead code in `PROGRESS.md`; do not delete it unless asked

Repository-specific rule: do not write new implementation files under `solana_meme_scanner_codex_handoff/`.

## 4. Goal-Driven Execution
Convert implementation requests into verifiable goals.

For every non-trivial task, define:
- success criteria
- commands that prove success
- stop conditions
- expected files touched

Use this pattern:

```text
1. [small step] -> verify: [command or inspection]
2. [small step] -> verify: [command or inspection]
3. [small step] -> verify: [command or inspection]
```

Strong criteria let Codex loop independently. Weak criteria create drift.

## 5. Verification Loop
A task is not complete until verification succeeds or a real environment blocker is documented.

Preferred baseline checks:

```bash
python -m pip install -e .[dev]
python -m pytest
python -m app.cli --help
```

If local dependency installation is blocked, add or use root-level GitHub Actions CI and document:
- exact failed command
- exact error
- why CI is the fallback
- whether CI passed or is pending

## 6. Completion Report
At the end of the task, report only:
- files changed
- tests/commands run
- pass/fail status
- unresolved blockers or risks
- next recommended action

Do not claim success when tests did not run.
