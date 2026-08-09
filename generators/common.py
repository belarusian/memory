from __future__ import annotations

from collections.abc import Callable

from micromegas import GeneratorConfig, Scene, SeededRng, parse_config, write_scene

SceneBuilder = Callable[[GeneratorConfig, SeededRng], Scene]


def run_generator(description: str, builder: SceneBuilder, argv: list[str] | None = None) -> Scene:
    config = parse_config(description, argv=argv)
    rng = SeededRng(config.seed)
    scene = builder(config, rng)
    actual_output = write_scene(scene, config.output)
    print(actual_output)
    return scene
