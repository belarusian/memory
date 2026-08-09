from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass
class SeededRng:
    seed: int

    def __post_init__(self) -> None:
        self._rng = random.Random(self.seed)

    def split(self, label: str) -> "SeededRng":
        payload = f"{self.seed}:{label}".encode("utf-8")
        digest = hashlib.sha256(payload).digest()
        new_seed = int.from_bytes(digest[:8], "big")
        return SeededRng(new_seed)

    def randint(self, low: int, high: int) -> int:
        return self._rng.randint(low, high)

    def uniform(self, low: float, high: float) -> float:
        return self._rng.uniform(low, high)

    def choice(self, items: Sequence[T]) -> T:
        return self._rng.choice(items)

    def maybe(self, probability: float) -> bool:
        return self._rng.random() < probability

    def weighted_choice(self, choices: Sequence[tuple[T, float]]) -> T:
        total = sum(weight for _, weight in choices)
        marker = self._rng.uniform(0, total)
        cursor = 0.0
        for item, weight in choices:
            cursor += weight
            if marker <= cursor:
                return item
        return choices[-1][0]
