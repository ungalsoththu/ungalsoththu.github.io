#!/usr/bin/env bash
# Regenerate subsites from workspace notes and publish to ungalsoththu.github.io.
# The GitHub Action (deploy.yml) builds+deploys on push to main.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"
python3 scripts/build.py
git add public scripts
if git diff --cached --quiet; then
  echo "publish: no changes"
  exit 0
fi
git commit -q -m "daily briefs: $(date +%F)"
if git push origin main; then
  echo "publish: pushed — Pages Action deploying (~2 min)"
else
  echo "publish: PUSH FAILED (check ungalsoththu account access); archive note is safe locally" >&2
  exit 1
fi
