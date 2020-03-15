"""
cards.py

Allows you to generate a deck of playing cards

# TODO: Fix the __repr__() in Deck class to print cards correctly
# TODO: Amend to allow generation of rigged cards based on specification

"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.suit}{self.rank}"


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "C D H S".split()


def make_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_deck)
