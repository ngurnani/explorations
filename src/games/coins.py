"""
coins.py

Allows you to generate one or several coins with certain probability of landing on H or T
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Coin:
    face: str = field(default="H")
    prob: float = field(default=0.5)


@dataclass
class Coins:
    n: int
    coins = List[Coin]
