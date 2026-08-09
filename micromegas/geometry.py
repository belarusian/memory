from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Vec3:
    x: float
    y: float
    z: float

    def scaled(self, factor: float) -> "Vec3":
        return Vec3(self.x * factor, self.y * factor, self.z * factor)


@dataclass
class Transform:
    location: Vec3 = field(default_factory=lambda: Vec3(0.0, 0.0, 0.0))
    rotation: Vec3 = field(default_factory=lambda: Vec3(0.0, 0.0, 0.0))
    scale: Vec3 = field(default_factory=lambda: Vec3(1.0, 1.0, 1.0))


@dataclass
class Primitive:
    kind: str
    params: dict[str, float]


@dataclass
class SceneObject:
    name: str
    primitive: Primitive | None = None
    transform: Transform = field(default_factory=Transform)
    material: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    children: list["SceneObject"] = field(default_factory=list)

    def add(self, *objects: "SceneObject") -> "SceneObject":
        self.children.extend(objects)
        return self


@dataclass
class Scene:
    name: str
    seed: int
    family: str
    objects: list[SceneObject] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add(self, *objects: SceneObject) -> "Scene":
        self.objects.extend(objects)
        return self


def root(name: str) -> SceneObject:
    return SceneObject(name=name)


def cylinder(name: str, radius: float, depth: float, material: str | None = None) -> SceneObject:
    return SceneObject(name=name, primitive=Primitive("cylinder", {"radius": radius, "depth": depth}), material=material)


def sphere(name: str, radius: float, material: str | None = None) -> SceneObject:
    return SceneObject(name=name, primitive=Primitive("sphere", {"radius": radius}), material=material)


def box(name: str, x: float, y: float, z: float, material: str | None = None) -> SceneObject:
    return SceneObject(name=name, primitive=Primitive("box", {"x": x, "y": y, "z": z}), material=material)


def torus(name: str, major_radius: float, minor_radius: float, material: str | None = None) -> SceneObject:
    return SceneObject(
        name=name,
        primitive=Primitive("torus", {"major_radius": major_radius, "minor_radius": minor_radius}),
        material=material,
    )


def cone(name: str, radius1: float, radius2: float, depth: float, material: str | None = None) -> SceneObject:
    return SceneObject(
        name=name,
        primitive=Primitive("cone", {"radius1": radius1, "radius2": radius2, "depth": depth}),
        material=material,
    )
