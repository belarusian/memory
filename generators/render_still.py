from __future__ import annotations

import argparse
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
    scene.render.filepath = output_path
    scene.frame_set(1)
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    main()
