from __future__ import annotations

from dataclasses import dataclass

from .randomness import SeededRng


@dataclass(frozen=True)
class Material:
    name: str
    base_color: tuple[float, float, float]
    metallic: float
    roughness: float


DEFAULT_PALETTE = {
    "brass": Material("brass", (0.73, 0.58, 0.24), 0.85, 0.25),
    "obsidian": Material("obsidian", (0.08, 0.08, 0.1), 0.2, 0.15),
    "ivory": Material("ivory", (0.92, 0.91, 0.84), 0.05, 0.65),
    "emerald": Material("emerald", (0.1, 0.45, 0.3), 0.1, 0.35),
    "silver": Material("silver", (0.75, 0.75, 0.78), 0.95, 0.12),
    "ceramic": Material("ceramic", (0.86, 0.86, 0.9), 0.0, 0.7),
}


def choose_primary_material(rng: SeededRng) -> Material:
    return rng.choice(list(DEFAULT_PALETTE.values()))


def choose_secondary_material(rng: SeededRng, exclude: str) -> Material:
    pool = [value for key, value in DEFAULT_PALETTE.items() if key != exclude]
    return rng.choice(pool)


def palette_dict() -> dict[str, dict[str, float | tuple[float, float, float] | str]]:
    return {
        key: {
            "name": material.name,
            "base_color": material.base_color,
            "metallic": material.metallic,
            "roughness": material.roughness,
        }
        for key, material in DEFAULT_PALETTE.items()
    }
