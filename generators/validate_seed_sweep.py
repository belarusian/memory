from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.cli import GeneratorConfig
from micromegas.io import scene_to_dict
from micromegas.randomness import SeededRng

from generators.alien_measure import build_scene as build_alien_measure
from generators.cosmic_necklace import build_scene as build_cosmic_necklace
from generators.empty_book import build_scene as build_empty_book
from generators.great_microscope import build_scene as build_great_microscope
from generators.scale_reliquary import build_scene as build_scale_reliquary
from generators.sirian_instrument import build_scene as build_sirian_instrument


def _count_primitives(objects: list[dict]) -> Counter:
    counter: Counter = Counter()

    def walk(obj: dict) -> None:
        primitive = obj.get("primitive")
        if primitive:
            counter[primitive["kind"]] += 1
        for child in obj.get("children", []):
            walk(child)

    for obj in objects:
        walk(obj)
    return counter


def _blank_pages_invariant(scene_data: dict) -> bool:
    if scene_data["family"] != "empty_book":
        return True

    blank_pages = 0

    def walk(obj: dict) -> None:
        nonlocal blank_pages
        if obj["name"].startswith("page_"):
            metadata = obj.get("metadata", {})
            if metadata.get("is_blank") and metadata.get("content", None) == "":
                blank_pages += 1
        for child in obj.get("children", []):
            walk(child)

    for obj in scene_data["objects"]:
        walk(obj)
    return blank_pages > 0


def main() -> None:
    builders = {
        "great_microscope": build_great_microscope,
        "empty_book": build_empty_book,
        "sirian_instrument": build_sirian_instrument,
        "cosmic_necklace": build_cosmic_necklace,
        "alien_measure": build_alien_measure,
        "scale_reliquary": build_scale_reliquary,
    }
    seeds = list(range(100, 120))
    report = {}

    for name, builder in builders.items():
        signatures = set()
        primitive_profiles = []
        invariant_ok = True

        for seed in seeds:
            cfg = GeneratorConfig(seed=seed, output=f"/tmp/micromegas-validation/{name}-{seed}.json", style="validation", complexity=4)
            scene = builder(cfg, SeededRng(seed))
            data = scene_to_dict(scene)
            primitive_counts = _count_primitives(data["objects"])
            primitive_profiles.append(dict(sorted(primitive_counts.items())))
            signatures.add(tuple(sorted(primitive_counts.items())))
            invariant_ok = invariant_ok and _blank_pages_invariant(data)

        report[name] = {
            "seed_count": len(seeds),
            "unique_signatures": len(signatures),
            "variation_ratio": len(signatures) / len(seeds),
            "blank_invariant_ok": invariant_ok,
            "sample_profile": primitive_profiles[0],
        }

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
