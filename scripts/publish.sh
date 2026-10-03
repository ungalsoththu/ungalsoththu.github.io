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
if [ -n "${UNGALSOTHTHU_GH_TOKEN:-}" ]; then
  # Reset ambient credential helpers (gh/srikanthlogic) and auth as ungalsoththu.
  PUSH_OK=$(git -c credential.helper= \
    -c "credential.helper=!f() { echo username=x-access-token; echo password=${UNGALSOTHTHU_GH_TOKEN}; }; f" \
    push origin main >/dev/null 2>&1 && echo yes || echo no)
else
  PUSH_OK=$(git push origin main >/dev/null 2>&1 && echo yes || echo no)
fi
if [ "$PUSH_OK" = yes ]; then
  echo "publish: pushed — Pages Action deploying (~2 min)"
else
  echo "publish: PUSH FAILED (check UNGALSOTHTHU_GH_TOKEN); committed locally" >&2
  exit 1
fi
