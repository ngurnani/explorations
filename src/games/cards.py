"""
cards.py

Allows you to generate a deck of playing cards

# TODO: Amend to allow generation of rigged cards based on specification

"""
from dataclasses import dataclass, field
from typing import List

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "C D H S".split()


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)

    def __str__(self):
        return f"{self.suit}{self.rank}"


def make_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_deck)

    def __repr__(self):
        cards = ", ".join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"
