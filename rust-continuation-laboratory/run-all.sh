#!/usr/bin/env bash
set -euo pipefail
for n in $(seq -w 1 24); do
  echo
  echo "========== exp$n =========="
  cargo run --quiet -p "$(awk -F'"' '/^name =/{print $2; exit}' exp$n/Cargo.toml)"
done
