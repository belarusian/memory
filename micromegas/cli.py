from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class GeneratorConfig:
    seed: int
    output: str
    style: str
    complexity: int


def build_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--seed", type=int, required=True, help="Deterministic seed.")
    parser.add_argument("--output", type=str, required=True, help="Output scene path (.json or .blend).")
    parser.add_argument("--style", type=str, default="default", help="Stylistic family selector.")
    parser.add_argument("--complexity", type=int, default=3, choices=range(1, 8), help="Grammar complexity level.")
    return parser


def parse_config(description: str, argv: list[str] | None = None) -> GeneratorConfig:
    parser = build_parser(description)
    if argv is None:
        argv = sys.argv[1:]
        if "--" in argv:
            argv = argv[argv.index("--") + 1 :]
    args = parser.parse_args(argv)
    return GeneratorConfig(seed=args.seed, output=args.output, style=args.style, complexity=args.complexity)
