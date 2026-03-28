#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

source .env
export KAGGLE_USERNAME KAGGLE_API_TOKEN

USERNAME="$KAGGLE_USERNAME"
COMPETITION="$KAGGLE_COMPETITION_NAME"
SLUG="${COMPETITION}-sub"
SUB_DIR="sub"

cat > "${SUB_DIR}/kernel-metadata.json" <<EOF
{
  "id": "${USERNAME}/${SLUG}",
  "title": "${SLUG}",
  "code_file": "sub.ipynb",
  "language": "python",
  "kernel_type": "notebook",
  "is_private": "true",
  "enable_gpu": "true",
  "enable_tpu": "false",
  "enable_internet": "false",
  "dataset_sources": [
    "${USERNAME}/${COMPETITION}-codes"
  ],
  "competition_sources": ["${COMPETITION}"],
  "kernel_sources": ["${USERNAME}/${COMPETITION}-deps"],
  "model_sources": []
}
EOF

echo "Pushing kernel: ${USERNAME}/${SLUG}"
kaggle kernels push -p "$SUB_DIR"

echo "Done!"
