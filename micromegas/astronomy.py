from __future__ import annotations

from .geometry import SceneObject, Transform, Vec3, box, cone, sphere, torus
from .randomness import SeededRng


STAR_GLYPHS = ["Sirius", "Canopus", "Aldebaran", "Rigel", "Polaris", "Vega"]


def orbital_system(rng: SeededRng, label: str, planet_count: int) -> SceneObject:
    system = SceneObject(name=f"{label}_orbital_system")
    star = sphere(f"{label}_star", radius=rng.uniform(0.2, 0.45), material="emerald")
    system.add(star)
    for index in range(planet_count):
        distance = 0.45 + index * rng.uniform(0.22, 0.4)
        orbit = torus(f"{label}_orbit_{index}", major_radius=distance, minor_radius=0.01, material="silver")
        orbit.transform = Transform(scale=Vec3(1.0, 1.0, rng.uniform(0.75, 1.35)))
        planet = sphere(f"{label}_planet_{index}", radius=rng.uniform(0.04, 0.14), material="ivory")
        planet.transform = Transform(location=Vec3(distance, 0.0, rng.uniform(-0.07, 0.07)))
        system.add(orbit, planet)
    return system


def calibration_glyph_ring(rng: SeededRng, label: str, ring_radius: float, glyph_count: int) -> SceneObject:
    ring = torus(f"{label}_calibration_ring", major_radius=ring_radius, minor_radius=0.02, material="brass")
    glyphs = SceneObject(name=f"{label}_glyphs")
    for idx in range(glyph_count):
        marker = cone(f"{label}_glyph_marker_{idx}", radius1=0.03, radius2=0.0, depth=0.08, material="silver")
        marker.metadata["glyph"] = rng.choice(STAR_GLYPHS)
        marker.transform = Transform(location=Vec3(0.0, ring_radius, 0.0), rotation=Vec3(0.0, 0.0, idx * (6.28318 / glyph_count)))
        glyphs.add(marker)
    return SceneObject(name=f"{label}_calibration").add(ring, glyphs)


def celestial_pointer(rng: SeededRng, label: str) -> SceneObject:
    pointer = SceneObject(name=f"{label}_celestial_pointer")
    shaft = box(f"{label}_pointer_shaft", x=0.04, y=0.4, z=0.04, material="silver")
    tip = cone(f"{label}_pointer_tip", radius1=0.06, radius2=0.0, depth=0.2, material="emerald")
    tip.transform = Transform(location=Vec3(0.0, 0.3, 0.0), rotation=Vec3(1.5708, 0.0, 0.0))
    pointer.metadata["target"] = rng.choice(STAR_GLYPHS)
    pointer.add(shaft, tip)
    return pointer
