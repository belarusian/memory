from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, cylinder, sphere
from micromegas.mechanisms import (
    articulated_support_arms,
    astronomical_calibration_mechanism,
    decorative_geometric_structures,
    nested_lens_assemblies,
)
from micromegas.randomness import SeededRng
from micromegas.scale import make_reference_object

from generators.common import run_generator


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    scene = Scene(name="micromegas_sirian_instrument", seed=config.seed, family="sirian_instrument")
    core = cylinder("sirian_core_spine", radius=rng.uniform(0.2, 0.6), depth=rng.uniform(2.5, 5.5), material="brass")
    core.transform = Transform(rotation=Vec3(1.5708, 0.0, 0.0))
    crown = sphere("sirian_core_crown", radius=rng.uniform(0.4, 0.8), material="emerald")
    crown.transform = Transform(location=Vec3(0.0, 0.0, rng.uniform(1.0, 2.5)))

    apparatus = SceneObject("sirian_apparatus")
    apparatus.add(core, crown)
    apparatus.add(articulated_support_arms(rng.split("arms"), "sirian", arm_count=rng.randint(3, 8), material="silver"))
    apparatus.add(nested_lens_assemblies(rng.split("lenses"), "sirian", count=rng.randint(5, 11), material="obsidian"))
    apparatus.add(astronomical_calibration_mechanism(rng.split("calibration"), "sirian"))
    apparatus.add(decorative_geometric_structures(rng.split("ornament"), "sirian", complexity=config.complexity + 1))

    alien_reference = make_reference_object("sirian_height_reference", category="city")
    alien_reference.transform = Transform(location=Vec3(0.0, -2.0, -1.0), scale=Vec3(0.25, 0.25, 0.25))

    scene.add(apparatus, alien_reference)
    scene.metadata.update({"style": config.style, "complexity": config.complexity})
    return scene


def main() -> None:
    run_generator("Generate a seeded Sirian impossible astronomical instrument.", build_scene)


if __name__ == "__main__":
    main()
