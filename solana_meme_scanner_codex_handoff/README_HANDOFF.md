# Manual Setup Before Handing Off To Codex Cloud

## 1. Create GitHub Repo

Create a new GitHub repo named:

```txt
solana-meme-launch-scanner
```

Keep it empty or initialize it with a README. Either is fine.

## 2. Upload These Files

Put these files/folders at the root of the repo:

```txt
AGENTS.md
PLANS.md
PROGRESS.md
STARTING_PROMPT.md
README_HANDOFF.md
goals/
skills/
```

Final repo root should look like:

```txt
solana-meme-launch-scanner/
  AGENTS.md
  PLANS.md
  PROGRESS.md
  STARTING_PROMPT.md
  README_HANDOFF.md
  goals/
    milestone-1.goal.md
    milestone-2.goal.md
    milestone-3.goal.md
    milestone-4.goal.md
    milestone-5.goal.md
  skills/
    launch-phase-data-model/
      SKILL.md
    api-collection/
      SKILL.md
    phase-detection-backtest/
      SKILL.md
```

## 3. Commit And Push

```bash
git add .
git commit -m "bootstrap codex operating files"
git push
```

## 4. Open Codex Cloud

Open Codex Cloud/Web and connect it to the GitHub repository.

Codex Cloud can work in its own cloud environment, so it can continue while your laptop is closed. Local Codex CLI cannot reliably do that if your Mac sleeps.

## 5. Send One Message To Codex

Paste the content of `STARTING_PROMPT.md`.

If the Codex interface supports `/plan`, start with:

```txt
/plan
```

Then paste the prompt.

If the interface supports `/goal`, use the full goal from:

```txt
goals/milestone-1.goal.md
```

If `/goal` is unavailable, just paste `STARTING_PROMPT.md`; the files still force a milestone workflow.

## 6. What You Should Expect Back

Codex should first create:

```txt
IMPLEMENTATION_PLAN.md
```

Then it should implement only Milestone 1.

Do not let it jump to API collectors, live scanning, holder intelligence, dashboards, or trading logic before Milestone 1 passes.
