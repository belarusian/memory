from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.astronomy import orbital_system
from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, sphere, torus
from micromegas.randomness import SeededRng
from micromegas.scale import magnify, miniaturize

from generators.common import run_generator


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    scene = Scene(name="micromegas_cosmic_necklace", seed=config.seed, family="cosmic_necklace")
    thread = torus("necklace_thread", major_radius=rng.uniform(2.0, 4.0), minor_radius=rng.uniform(0.04, 0.09), material="silver")
    necklace = SceneObject("cosmic_necklace")
    necklace.add(thread)

    bead_count = rng.randint(5, 15)
    for idx in range(bead_count):
        bead_system = orbital_system(rng.split(f"bead-{idx}"), f"bead_{idx}", planet_count=rng.randint(1, 6))
        bead = sphere(f"bead_shell_{idx}", radius=rng.uniform(0.2, 0.6), material="ivory")
        bead.transform = Transform(location=Vec3(rng.uniform(-3.0, 3.0), rng.uniform(-3.0, 3.0), rng.uniform(-0.5, 0.5)))
        bead_system.transform = Transform(location=Vec3(0.0, 0.0, 0.0), scale=Vec3(0.25, 0.25, 0.25))
        bead.add(bead_system)
        necklace.add(bead)

    macro = magnify(necklace, factor=2.0, suffix="macro")
    micro = miniaturize(necklace, factor=50.0, suffix="micro")
    micro.transform = Transform(location=Vec3(0.0, 0.0, -1.0), scale=Vec3(0.04, 0.04, 0.04))

    scene.add(necklace, macro, micro)
    scene.metadata.update({"style": config.style, "complexity": config.complexity, "bead_count": bead_count})
    return scene


def main() -> None:
    run_generator("Generate a seeded cosmic necklace of planetary beads.", build_scene)


if __name__ == "__main__":
    main()
