from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.astronomy import celestial_pointer
from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, box, cylinder, torus
from micromegas.mechanisms import measurement_rings
from micromegas.randomness import SeededRng

from generators.common import run_generator


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    scene = Scene(name="micromegas_alien_measure", seed=config.seed, family="alien_measure")
    instrument = SceneObject("alien_measurement_stack")

    spine = cylinder("spine", radius=0.12, depth=rng.uniform(2.0, 4.8), material="brass")
    spine.transform = Transform(rotation=Vec3(1.5708, 0.0, 0.0))
    caliper = box("caliper_frame", x=rng.uniform(0.8, 1.6), y=0.14, z=rng.uniform(0.8, 1.6), material="silver")
    sextant_arc = torus("sextant_arc", major_radius=rng.uniform(0.6, 1.4), minor_radius=0.04, material="obsidian")

    ticks = SceneObject("ticks")
    for idx in range(rng.randint(16, 48)):
        tick = box(f"tick_{idx}", x=0.02, y=rng.uniform(0.05, 0.12), z=0.02, material="ivory")
        tick.transform = Transform(location=Vec3(0.0, rng.uniform(0.5, 1.5), 0.0), rotation=Vec3(0.0, 0.0, idx * 6.28318 / 36))
        tick.metadata["unit"] = f"{rng.randint(200, 900)}-sir"
        ticks.add(tick)

    instrument.add(spine, caliper, sextant_arc, measurement_rings(rng.split("rings"), "alien_measure", ring_count=rng.randint(2, 5)), ticks)
    instrument.add(celestial_pointer(rng.split("pointer"), "alien_measure"))

    scene.add(instrument)
    scene.metadata.update({"style": config.style, "complexity": config.complexity})
    return scene


def main() -> None:
    run_generator("Generate a seeded alien measurement apparatus with non-human units.", build_scene)


if __name__ == "__main__":
    main()
