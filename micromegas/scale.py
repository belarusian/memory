from __future__ import annotations

from dataclasses import replace

from .geometry import SceneObject, Transform, Vec3, box, sphere


def _scaled_transform(transform: Transform, factor: float) -> Transform:
    return Transform(
        location=transform.location.scaled(factor),
        rotation=replace(transform.rotation),
        scale=transform.scale.scaled(factor),
    )


def magnify(obj: SceneObject, factor: float, suffix: str = "magnified") -> SceneObject:
    clone = SceneObject(
        name=f"{obj.name}_{suffix}",
        primitive=obj.primitive,
        transform=_scaled_transform(obj.transform, factor),
        material=obj.material,
        metadata={**obj.metadata, "scale_operation": "magnify", "factor": factor},
    )
    for child in obj.children:
        clone.add(magnify(child, factor, suffix))
    return clone


def miniaturize(obj: SceneObject, factor: float, suffix: str = "miniature") -> SceneObject:
    if factor <= 0:
        raise ValueError("factor must be positive")
    return magnify(obj, 1.0 / factor, suffix=suffix)


def nest(container: SceneObject, contained: SceneObject, offset: Vec3 | None = None) -> SceneObject:
    nested = SceneObject(name=f"{container.name}_nested")
    contained_copy = magnify(contained, 1.0, suffix="nested_copy")
    if offset is not None:
        contained_copy.transform = Transform(
            location=offset,
            rotation=contained_copy.transform.rotation,
            scale=contained_copy.transform.scale,
        )
    nested.add(container, contained_copy)
    return nested


def repeat_at_scale(obj: SceneObject, scales: list[float], label: str = "scaled_series") -> SceneObject:
    series = SceneObject(name=f"{obj.name}_{label}")
    for idx, factor in enumerate(scales):
        replica = magnify(obj, factor, suffix=f"x{factor:g}")
        replica.transform = Transform(
            location=Vec3(0.0, idx * (1.5 + factor), 0.0),
            rotation=replica.transform.rotation,
            scale=replica.transform.scale,
        )
        replica.metadata["scale_index"] = idx
        series.add(replica)
    return series


def make_reference_object(name: str, category: str = "human") -> SceneObject:
    if category == "human":
        ref = box(name, x=0.15, y=0.15, z=1.75, material="ceramic")
    elif category == "city":
        ref = box(name, x=2.5, y=2.5, z=4.0, material="ceramic")
    elif category == "planet":
        ref = sphere(name, radius=1.0, material="ivory")
    else:
        ref = box(name, x=0.5, y=0.5, z=0.5, material="ceramic")
    ref.metadata["reference_category"] = category
    return ref
