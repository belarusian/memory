from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from micromegas.cli import GeneratorConfig
from micromegas.geometry import Scene, SceneObject, Transform, Vec3, root
from micromegas.materials import choose_primary_material, choose_secondary_material
from micromegas.mechanisms import (
    articulated_support_arms,
    astronomical_calibration_mechanism,
    decorative_geometric_structures,
    inaccessible_control_surfaces,
    measurement_rings,
    nested_lens_assemblies,
    primary_optical_axis,
    specimen_chamber,
)
from micromegas.randomness import SeededRng
from micromegas.scale import make_reference_object, miniaturize, nest

from generators.common import run_generator


def build_scene(config: GeneratorConfig, rng: SeededRng) -> Scene:
    primary_material = choose_primary_material(rng)
    secondary_material = choose_secondary_material(rng, exclude=primary_material.name)

    scene = Scene(name="micromegas_great_microscope", seed=config.seed, family="great_microscope")
    scene.metadata.update(
        {
            "style": config.style,
            "complexity": config.complexity,
            "grammar": [
                "primary_optical_axis",
                "articulated_support_arms",
                "specimen_chamber",
                "nested_lens_assemblies",
                "measurement_rings",
                "astronomical_calibration_mechanism",
                "inaccessible_control_surfaces",
                "decorative_geometric_structures",
            ],
        }
    )

    instrument = root("great_microscope_instrument")
    instrument.add(primary_optical_axis(rng.split("axis"), "microscope", primary_material.name))
    instrument.add(
        articulated_support_arms(
            rng.split("arms"),
            "microscope",
            arm_count=rng.randint(2, 7),
            material=secondary_material.name,
        )
    )
    instrument.add(specimen_chamber(rng.split("chamber"), "microscope", primary_material.name))
    instrument.add(
        nested_lens_assemblies(
            rng.split("lenses"),
            "microscope",
            count=rng.randint(max(3, config.complexity), config.complexity + 6),
            material=secondary_material.name,
        )
    )
    instrument.add(measurement_rings(rng.split("rings"), "microscope", ring_count=rng.randint(2, config.complexity + 3)))
    instrument.add(astronomical_calibration_mechanism(rng.split("calibration"), "microscope"))
    instrument.add(inaccessible_control_surfaces(rng.split("controls"), "microscope"))
    instrument.add(decorative_geometric_structures(rng.split("ornament"), "microscope", complexity=config.complexity))

    specimen_reference = make_reference_object("earth_reference", category="planet")
    specimen_reference.transform = Transform(location=Vec3(0.0, 0.0, -0.2), scale=Vec3(0.2, 0.2, 0.2))
    human_reference = miniaturize(make_reference_object("human_reference", category="human"), factor=2000.0)
    human_reference.transform = Transform(location=Vec3(0.0, 0.3, 0.05), scale=Vec3(0.001, 0.001, 0.001))

    chamber_with_references = nest(specimen_reference, human_reference, offset=Vec3(0.0, 0.0, 0.5))
    chamber_with_references.metadata["joke"] = "observer_scale_reversal"

    scene.add(instrument, chamber_with_references)
    return scene


def main() -> None:
    run_generator("Generate a seeded Great Microscope procedural family artifact.", build_scene)


if __name__ == "__main__":
    main()
