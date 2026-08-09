from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, box, cylinder, sphere
from micromegas.mechanisms import decorative_geometric_structures
from micromegas.randomness import SeededRng
from micromegas.scale import repeat_at_scale

from generators.common import run_generator


def _blank_page_block(rng: SeededRng, page_count: int) -> SceneObject:
    block = SceneObject(name="page_block")
    for idx in range(page_count):
        page = box(
            f"page_{idx}",
            x=rng.uniform(0.8, 1.3),
            y=rng.uniform(0.01, 0.03),
            z=rng.uniform(1.2, 1.8),
            material="ivory",
        )
        page.transform = Transform(location=Vec3(0.0, idx * 0.012, 0.0))
        page.metadata["content"] = ""
        page.metadata["is_blank"] = True
        block.add(page)
    return block


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    scene = Scene(name="micromegas_empty_book", seed=config.seed, family="empty_book")
    cover = box("cover", x=1.6, y=0.2, z=2.2, material="obsidian")
    clasp_count = rng.randint(1, 4)
    clasps = SceneObject(name="clasps")
    for idx in range(clasp_count):
        clasp = cylinder(f"clasp_{idx}", radius=0.05, depth=0.4, material="brass")
        clasp.transform = Transform(location=Vec3((-0.6 + idx * 0.4), 0.1, 1.15), rotation=Vec3(1.5708, 0.0, 0.0))
        clasps.add(clasp)

    hinges = SceneObject(name="hinges")
    for idx in range(rng.randint(2, 5)):
        hinge = sphere(f"hinge_{idx}", radius=0.04, material="silver")
        hinge.transform = Transform(location=Vec3(-0.8, 0.05 + idx * 0.07, -1.1))
        hinges.add(hinge)

    page_count = rng.randint(36, 140)
    page_block = _blank_page_block(rng.split("pages"), page_count)
    ornament = decorative_geometric_structures(rng.split("ornament"), "empty_book", complexity=config.complexity)

    series = repeat_at_scale(cover, [1.0, 2.0, 4.0], label="magnitudes")

    volume = SceneObject(name="empty_volume").add(cover, clasps, hinges, page_block, ornament, series)
    scene.add(volume)
    scene.metadata.update(
        {
            "style": config.style,
            "complexity": config.complexity,
            "invariants": {
                "all_pages_blank": True,
                "blank_content_value": "",
            },
            "page_count": page_count,
        }
    )
    return scene


def main() -> None:
    run_generator("Generate a seeded Empty Book artifact with invariant blank pages.", build_scene)


if __name__ == "__main__":
    main()
