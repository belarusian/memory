from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .geometry import Scene, SceneObject
from .materials import palette_dict


def _object_to_dict(obj: SceneObject) -> dict[str, Any]:
    return {
        "name": obj.name,
        "primitive": None
        if obj.primitive is None
        else {
            "kind": obj.primitive.kind,
            "params": obj.primitive.params,
        },
        "transform": {
            "location": [obj.transform.location.x, obj.transform.location.y, obj.transform.location.z],
            "rotation": [obj.transform.rotation.x, obj.transform.rotation.y, obj.transform.rotation.z],
            "scale": [obj.transform.scale.x, obj.transform.scale.y, obj.transform.scale.z],
        },
        "material": obj.material,
        "metadata": obj.metadata,
        "children": [_object_to_dict(child) for child in obj.children],
    }


def scene_to_dict(scene: Scene) -> dict[str, Any]:
    return {
        "name": scene.name,
        "seed": scene.seed,
        "family": scene.family,
        "metadata": scene.metadata,
        "materials": palette_dict(),
        "objects": [_object_to_dict(obj) for obj in scene.objects],
    }


def write_scene(scene: Scene, output_path: str) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == ".blend":
        try:
            from . import blender_backend

            blender_backend.write_blend(scene, path)
            return path
        except Exception:
            fallback = path.with_suffix(".json")
            fallback.write_text(json.dumps(scene_to_dict(scene), indent=2), encoding="utf-8")
            return fallback
    path.write_text(json.dumps(scene_to_dict(scene), indent=2), encoding="utf-8")
    return path
