from __future__ import annotations

import argparse
import math
import sys


def parse_output_arg() -> str:
    argv = sys.argv[1:]
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    parser = argparse.ArgumentParser(description="Render a single still image from the current Blender scene.")
    parser.add_argument("--output", required=True, help="Output image path")
    args = parser.parse_args(argv)
    return args.output


def main() -> None:
    import bpy

    output_path = parse_output_arg()
    scene = bpy.context.scene
    if scene.camera is None:
        bpy.ops.object.camera_add(location=(6.0, -6.0, 4.0), rotation=(math.radians(60.0), 0.0, math.radians(45.0)))
        scene.camera = bpy.context.object
    if not any(obj.type == "LIGHT" for obj in scene.objects):
        bpy.ops.object.light_add(type="SUN", location=(4.0, -4.0, 8.0))
    scene.render.filepath = output_path
    scene.frame_set(1)
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    main()
