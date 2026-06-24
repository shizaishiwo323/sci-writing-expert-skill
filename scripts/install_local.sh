#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_ROOT="${HOME}/.agents/skills"
DEST="${DEST_ROOT}/sci-writing-expert"

mkdir -p "${DEST_ROOT}"

if [[ -e "${DEST}" || -L "${DEST}" ]]; then
  echo "Destination already exists: ${DEST}" >&2
  echo "Remove it or choose a different installation method." >&2
  exit 1
fi

ln -s "${SOURCE_DIR}" "${DEST}"
echo "Installed by symlink: ${DEST} -> ${SOURCE_DIR}"
echo "Restart Codex if the skill does not appear immediately."
