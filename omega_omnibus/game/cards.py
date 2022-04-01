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

    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
