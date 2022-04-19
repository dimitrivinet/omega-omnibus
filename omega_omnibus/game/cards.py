from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Card:
    """Representation of a card."""

    suit: Suit
    rank: Rank

    @classmethod
    def from_string(cls, card_str: str):
        """Create card from its string representation (ex: 'two of clubs')."""

        card_str = card_str.upper()

        try:
            rank_str, suit_str = card_str.split(" OF ")
            return cls(Suit[suit_str], Rank[rank_str])
        except Exception as e:
            raise ValueError("Failed to create card from provided string.") from e

    def __repr__(self):
        return f"{self.rank.name.title()} of {self.suit.name.title()}"


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
