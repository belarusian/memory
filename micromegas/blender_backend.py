from __future__ import annotations

from pathlib import Path

from .geometry import Scene, SceneObject


def _create_object(obj: SceneObject) -> None:
    import bpy

    if obj.primitive:
        kind = obj.primitive.kind
        params = obj.primitive.params
        if kind == "cylinder":
            bpy.ops.mesh.primitive_cylinder_add(radius=params["radius"], depth=params["depth"])
        elif kind == "sphere":
            bpy.ops.mesh.primitive_uv_sphere_add(radius=params["radius"])
        elif kind == "box":
            bpy.ops.mesh.primitive_cube_add(size=1)
            bpy.context.object.scale = (params["x"], params["y"], params["z"])
        elif kind == "torus":
            bpy.ops.mesh.primitive_torus_add(major_radius=params["major_radius"], minor_radius=params["minor_radius"])
        elif kind == "cone":
            bpy.ops.mesh.primitive_cone_add(radius1=params["radius1"], radius2=params["radius2"], depth=params["depth"])
        else:
            return

        active = bpy.context.object
        active.name = obj.name
        active.location = (obj.transform.location.x, obj.transform.location.y, obj.transform.location.z)
        active.rotation_euler = (obj.transform.rotation.x, obj.transform.rotation.y, obj.transform.rotation.z)
        active.scale = (active.scale[0] * obj.transform.scale.x, active.scale[1] * obj.transform.scale.y, active.scale[2] * obj.transform.scale.z)

    for child in obj.children:
        _create_object(child)


def write_blend(scene: Scene, output_path: Path) -> None:
    import bpy

    bpy.ops.wm.read_factory_settings(use_empty=True)
    for obj in scene.objects:
        _create_object(obj)
    bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
