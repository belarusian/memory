#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/outputs/micromegas"
JSON_DIR="${OUT_DIR}/json"
BLEND_DIR="${OUT_DIR}/blend"
IMAGE_DIR="${OUT_DIR}/images"
MANIFEST_PATH="${OUT_DIR}/manifest.json"

mkdir -p "${JSON_DIR}" "${BLEND_DIR}" "${IMAGE_DIR}"

GENERATORS=(
  "great_microscope"
  "empty_book"
  "sirian_instrument"
  "cosmic_necklace"
  "alien_measure"
  "scale_reliquary"
)

SEEDS=(1847 1776 1633 1911 2024 2401)

entries=()
for i in "${!GENERATORS[@]}"; do
  generator="${GENERATORS[$i]}"
  seed="${SEEDS[$i]}"
  script="${ROOT_DIR}/generators/${generator}.py"
  json_path="${JSON_DIR}/${generator}.json"
  blend_path="${BLEND_DIR}/${generator}.blend"
  image_path="${IMAGE_DIR}/${generator}.png"

  python "${script}" --seed "${seed}" --output "${json_path}" --style sample --complexity 4 >/dev/null

  if command -v blender >/dev/null 2>&1; then
    blender -b --python "${script}" -- --seed "${seed}" --output "${blend_path}" --style sample --complexity 4 >/dev/null
    blender -b "${blend_path}" --python "${ROOT_DIR}/generators/render_still.py" -- --output "${image_path}" >/dev/null
    image_rel="outputs/micromegas/images/${generator}.png"
  else
    image_rel=""
  fi

  entries+=("{\"name\":\"${generator}\",\"seed\":${seed},\"json\":\"outputs/micromegas/json/${generator}.json\",\"image\":\"${image_rel}\"}")
done

{
  printf '{\n  "artifacts": [\n'
  for idx in "${!entries[@]}"; do
    suffix=","
    if [[ "$idx" -eq $((${#entries[@]} - 1)) ]]; then
      suffix=""
    fi
    printf '    %s%s\n' "${entries[$idx]}" "${suffix}"
  done
  printf '  ]\n}\n'
} >"${MANIFEST_PATH}"

echo "Generated samples and manifest at ${OUT_DIR}"
