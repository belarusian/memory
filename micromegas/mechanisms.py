from __future__ import annotations

from .astronomy import calibration_glyph_ring
from .geometry import SceneObject, Transform, Vec3, box, cone, cylinder, sphere, torus
from .randomness import SeededRng


def primary_optical_axis(rng: SeededRng, label: str, material: str) -> SceneObject:
    depth = rng.uniform(3.0, 8.0)
    radius = rng.uniform(0.18, 0.45)
    axis = cylinder(f"{label}_optical_axis", radius=radius, depth=depth, material=material)
    axis.transform = Transform(rotation=Vec3(1.5708, 0.0, 0.0))
    return axis


def articulated_support_arms(rng: SeededRng, label: str, arm_count: int, material: str) -> SceneObject:
    arms = SceneObject(name=f"{label}_support_arms")
    for index in range(arm_count):
        segment_count = rng.randint(2, 5)
        arm = SceneObject(name=f"{label}_arm_{index}")
        length = rng.uniform(0.8, 1.6)
        for segment in range(segment_count):
            link = box(
                f"{label}_arm_{index}_segment_{segment}",
                x=rng.uniform(0.08, 0.18),
                y=length,
                z=rng.uniform(0.08, 0.18),
                material=material,
            )
            link.transform = Transform(location=Vec3(0.0, segment * (length * 0.85), 0.0), rotation=Vec3(0.0, 0.0, rng.uniform(-0.7, 0.7)))
            joint = sphere(f"{label}_arm_{index}_joint_{segment}", radius=rng.uniform(0.07, 0.16), material="silver")
            joint.transform = Transform(location=Vec3(0.0, segment * (length * 0.85), 0.0))
            arm.add(link, joint)
        arm.transform = Transform(
            location=Vec3(rng.uniform(-2.0, 2.0), rng.uniform(-2.0, 2.0), rng.uniform(-0.8, 0.8)),
            rotation=Vec3(rng.uniform(-1.0, 1.0), rng.uniform(-1.0, 1.0), rng.uniform(-3.14, 3.14)),
        )
        arms.add(arm)
    return arms


def specimen_chamber(rng: SeededRng, label: str, material: str) -> SceneObject:
    chamber = SceneObject(name=f"{label}_specimen_chamber")
    shell = sphere(f"{label}_chamber_shell", radius=rng.uniform(0.6, 1.2), material=material)
    shell.metadata["hollow"] = True
    cradle = torus(f"{label}_chamber_cradle", major_radius=rng.uniform(0.35, 0.7), minor_radius=0.05, material="silver")
    planet = sphere(f"{label}_specimen_planet", radius=rng.uniform(0.15, 0.32), material="ivory")
    planet.metadata["role"] = "specimen"
    chamber.add(shell, cradle, planet)
    return chamber


def nested_lens_assemblies(rng: SeededRng, label: str, count: int, material: str) -> SceneObject:
    assembly = SceneObject(name=f"{label}_lens_assemblies")
    base_radius = rng.uniform(0.3, 0.6)
    for idx in range(count):
        lens = torus(f"{label}_lens_{idx}", major_radius=base_radius + idx * rng.uniform(0.08, 0.22), minor_radius=rng.uniform(0.03, 0.09), material=material)
        lens.transform = Transform(rotation=Vec3(rng.uniform(0.0, 1.2), rng.uniform(0.0, 1.2), rng.uniform(0.0, 1.2)))
        assembly.add(lens)
    return assembly


def measurement_rings(rng: SeededRng, label: str, ring_count: int) -> SceneObject:
    rings = SceneObject(name=f"{label}_measurement_rings")
    for idx in range(ring_count):
        ring = calibration_glyph_ring(rng.split(f"ring-{idx}"), f"{label}_{idx}", ring_radius=rng.uniform(0.5, 1.3), glyph_count=rng.randint(8, 18))
        ring.transform = Transform(rotation=Vec3(rng.uniform(0.0, 3.14), rng.uniform(0.0, 3.14), rng.uniform(0.0, 3.14)))
        rings.add(ring)
    return rings


def astronomical_calibration_mechanism(rng: SeededRng, label: str) -> SceneObject:
    mechanism = SceneObject(name=f"{label}_astronomical_calibration")
    gyroscope = torus(f"{label}_gyro_core", major_radius=rng.uniform(0.4, 0.9), minor_radius=0.04, material="brass")
    spindle = cylinder(f"{label}_gyro_spindle", radius=0.03, depth=rng.uniform(0.8, 1.8), material="silver")
    spindle.transform = Transform(rotation=Vec3(1.5708, 0.0, 0.0))
    marker_count = rng.randint(3, 9)
    markers = SceneObject(name=f"{label}_star_markers")
    for idx in range(marker_count):
        marker = cone(f"{label}_star_marker_{idx}", radius1=0.05, radius2=0.0, depth=0.12, material="emerald")
        marker.transform = Transform(location=Vec3(0.0, rng.uniform(0.4, 1.0), 0.0), rotation=Vec3(0.0, 0.0, idx * 6.28318 / marker_count))
        markers.add(marker)
    mechanism.add(gyroscope, spindle, markers)
    return mechanism


def inaccessible_control_surfaces(rng: SeededRng, label: str) -> SceneObject:
    controls = SceneObject(name=f"{label}_inaccessible_controls")
    panel_count = rng.randint(3, 7)
    for idx in range(panel_count):
        panel = box(f"{label}_control_panel_{idx}", x=rng.uniform(0.22, 0.6), y=rng.uniform(0.07, 0.2), z=rng.uniform(0.22, 0.6), material="obsidian")
        panel.transform = Transform(location=Vec3(rng.uniform(-2.5, 2.5), rng.uniform(-2.5, 2.5), rng.uniform(1.0, 3.5)), rotation=Vec3(rng.uniform(0, 1), rng.uniform(0, 1), rng.uniform(0, 1)))
        panel.metadata["accessibility"] = "inaccessible"
        controls.add(panel)
    return controls


def decorative_geometric_structures(rng: SeededRng, label: str, complexity: int) -> SceneObject:
    ornaments = SceneObject(name=f"{label}_ornament")
    for idx in range(max(2, complexity * 2)):
        pick = rng.weighted_choice([("sphere", 2.0), ("torus", 2.0), ("cone", 1.0)])
        if pick == "sphere":
            shape = sphere(f"{label}_ornament_sphere_{idx}", radius=rng.uniform(0.05, 0.2), material="emerald")
        elif pick == "torus":
            shape = torus(f"{label}_ornament_torus_{idx}", major_radius=rng.uniform(0.08, 0.3), minor_radius=rng.uniform(0.01, 0.05), material="silver")
        else:
            shape = cone(f"{label}_ornament_cone_{idx}", radius1=rng.uniform(0.03, 0.1), radius2=0.0, depth=rng.uniform(0.06, 0.24), material="ivory")
        shape.transform = Transform(location=Vec3(rng.uniform(-3.0, 3.0), rng.uniform(-3.0, 3.0), rng.uniform(-1.0, 3.0)))
        ornaments.add(shape)
    return ornaments
