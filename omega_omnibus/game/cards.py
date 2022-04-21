from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Card:
    """Representation of a card."""

    suit: Suit
    rank: Rank


class Suit(Enum):
    """Enum of a card suit."""

    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class Rank(Enum):
    """Enum of a card rank."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
