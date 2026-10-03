#!/usr/bin/env bash
# Regenerate subsites from workspace notes and publish to ungalsoththu.github.io.
# The GitHub Action (deploy.yml) builds+deploys on push to main.
# Auth: UNGALSOTHTHU_GH_TOKEN env (Zo secret) — PAT of the ungalsoththu account.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"
python3 scripts/build.py
git add public scripts src
if git diff --cached --quiet; then
  echo "publish: no changes"
  exit 0
fi
git commit -q -m "daily briefs: $(date +%F)"
if [ -n "${UNGALSOTHTHU_GH_TOKEN:-}" ]; then
  PUSH_CMD=(git -c "credential.helper=!f() { echo username=x-access-token; echo password=${UNGALSOTHTHU_GH_TOKEN}; }; f" push origin main)
else
  echo "publish: UNGALSOTHTHU_GH_TOKEN not set — push will likely fail" >&2
  PUSH_CMD=(git push origin main)
fi
if "${PUSH_CMD[@]}"; then
  echo "publish: pushed — Pages Action deploying (~2 min)"
else
  echo "publish: PUSH FAILED; archive note is safe locally" >&2
  exit 1
fi
