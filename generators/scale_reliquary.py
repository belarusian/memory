from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, box, sphere
from micromegas.randomness import SeededRng
from micromegas.scale import make_reference_object, miniaturize, nest, repeat_at_scale

from generators.common import run_generator


def _reliquary_layer(rng: SeededRng, layer: int) -> SceneObject:
    shell = box(
        f"reliquary_shell_{layer}",
        x=1.2 + layer * 0.6,
        y=1.2 + layer * 0.6,
        z=1.2 + layer * 0.6,
        material=rng.choice(["obsidian", "brass", "silver"]),
    )
    core = sphere(f"reliquary_core_{layer}", radius=0.2 + layer * 0.1, material=rng.choice(["emerald", "ivory"]))
    return SceneObject(name=f"reliquary_layer_{layer}").add(shell, core)


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    scene = Scene(name="micromegas_scale_reliquary", seed=config.seed, family="scale_reliquary")
    layers = [_reliquary_layer(rng.split(f"layer-{idx}"), idx) for idx in range(config.complexity + 2)]

    stack = layers[0]
    for idx in range(1, len(layers)):
        stack = nest(layers[idx], stack, offset=Vec3(0.0, 0.0, 0.0))

    human_reference = make_reference_object("human_reference", category="human")
    city_reference = make_reference_object("city_reference", category="city")
    planet_reference = make_reference_object("planet_reference", category="planet")

    city_reference = miniaturize(city_reference, factor=60.0)
    city_reference.transform = Transform(location=Vec3(0.0, 0.0, 0.2), scale=Vec3(0.02, 0.02, 0.02))
    human_reference = miniaturize(human_reference, factor=200.0)
    human_reference.transform = Transform(location=Vec3(0.0, 0.0, 0.25), scale=Vec3(0.008, 0.008, 0.008))

    planetary_series = repeat_at_scale(planet_reference, [0.1, 1.0, 8.0], label="orders")

    scene.add(stack, city_reference, human_reference, planetary_series)
    scene.metadata.update({"style": config.style, "complexity": config.complexity, "layer_count": len(layers)})
    return scene


def main() -> None:
    run_generator("Generate a seeded nested scale reliquary artifact.", build_scene)


if __name__ == "__main__":
    main()
