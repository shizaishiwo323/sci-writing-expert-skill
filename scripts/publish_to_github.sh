#!/usr/bin/env bash
set -euo pipefail

OWNER="${1:-}"
REPO="${2:-sci-writing-expert-skill}"
VISIBILITY="${3:-public}"

if [[ -z "${OWNER}" ]]; then
  echo "Usage: $0 <github-owner> [repo-name] [public|private]" >&2
  exit 2
fi

if [[ "${VISIBILITY}" != "public" && "${VISIBILITY}" != "private" ]]; then
  echo "Visibility must be 'public' or 'private'." >&2
  exit 2
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git is required." >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required: https://cli.github.com/" >&2
  exit 1
fi

gh auth status >/dev/null

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

python scripts/validate_skill.py

if [[ ! -d .git ]]; then
  git init -b main
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "Create comprehensive SCI writing Codex skill"
fi

REMOTE="https://github.com/${OWNER}/${REPO}.git"

if gh repo view "${OWNER}/${REPO}" >/dev/null 2>&1; then
  if git remote get-url origin >/dev/null 2>&1; then
    git remote set-url origin "${REMOTE}"
  else
    git remote add origin "${REMOTE}"
  fi
else
  gh repo create "${OWNER}/${REPO}" "--${VISIBILITY}" \
    --description "Codex skill for SCI translation, polishing, logic diagnosis, and manuscript restructuring" \
    --source . \
    --remote origin
fi

git branch -M main
git push -u origin main

echo "Published: https://github.com/${OWNER}/${REPO}"
