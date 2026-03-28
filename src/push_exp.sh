#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

source .env
export KAGGLE_USERNAME KAGGLE_API_TOKEN

USERNAME="$KAGGLE_USERNAME"
SLUG="${KAGGLE_COMPETITION_NAME}-codes"
EXP_DIR="exp"
s
cat > "${EXP_DIR}/dataset-metadata.json" <<EOF
{
  "title": "${SLUG}",
  "id": "${USERNAME}/${SLUG}",
  "licenses": [{ "name": "CC0-1.0" }]
}
EOF

echo "Pushing dataset: ${USERNAME}/${SLUG}"
if ! kaggle datasets version -p "$EXP_DIR" -m "update codes"; then
  echo "datasets version failed — trying datasets create..."
  kaggle datasets create -p "$EXP_DIR"
fi

echo "Done!"
