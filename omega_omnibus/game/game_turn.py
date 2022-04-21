"""Onmibus game turn (where each player plays a card once, clockwise).
First player determines the preferred card suit.
"""

from typing import Dict, Optional, Tuple

from omega_omnibus.game.cards import Card, Suit


class Turn:
    """Represents a turn of Omnibus. Gets the trump card, the cards played
    during the turn, and calculates the points for each player."""

    num_players: int

    _dict: Dict[str, Tuple[Card, int]]
    trump: Card

    target_suit: Suit

    def __init__(self, num_players: int):
        """Creates an empty turn. Must set trump card and add cards
        one by one."""

        if num_players < 2:
            raise ValueError("Can't play a turn with less than two players.")

        self.num_players = num_players

        self._dict = {}

    def set_trump(self, trump: Card):
        """Set trump card for the turn."""

        if hasattr(self, "trump"):
            raise RuntimeError("Trump card was already set.")

        if not isinstance(trump, Card):
            raise TypeError

        self.trump = trump

    def add_card(self, player_id: str, card: Card):
        """Add new card to turn."""

        if not hasattr(self, "trump"):
            raise RuntimeError("Trump was not set before card was added.")

        if not isinstance(card, Card):
            raise TypeError

        if player_id in self._dict:
            raise RuntimeError(f"Player {player_id} already played a card.")

        if self._dict == {}:
            self.target_suit = card.suit

        card_score = self.card_score(card)

        self._dict[player_id] = (card, card_score)

    def calculate_score(self) -> Optional[str]:
        """Calculates turn score and returns winning player ID."""

        if not self.over:
            raise RuntimeError("Turn is not over, score cannot be calculated.")

        cards = list(self._dict.values())
        cards_copy = cards.copy()

        # remove scores that appear twice (omnibus)
        cards = list(
            filter(lambda x: cards_copy.count(x) == 1, cards)
        )
        winner_card = max(cards, default=0, key=lambda x: x[1])

        for player, played_card in self._dict.items():
            if played_card == winner_card:
                return player

        return None

    @property
    def over(self) -> bool:
        """Is turn over. Checks if everything was set properly for calculating score."""

        return hasattr(self, "trump") and len(self._dict.keys()) == self.num_players

    def card_score(self, card: Card) -> int:
        """Calculate the score of the card based on the current turn."""

        card_score = card.rank.value

        # if card suit is trump suit
        if card.suit == self.trump.suit:
            return card_score + 1000

        # if card is the first that was played or follows the target suit
        if self._dict == {} or card.suit == self.target_suit:
            return card_score + 100

        # if card doesn't follow any suit
        return card_score


if __name__ == "__main__":  # pragma: no cover
    print("creating test turn 1")
    t1 = Turn(4)

    print("setting trump")
    t1.set_trump(Card.from_string("two of clubs"))

    print("adding cards")
    t1.add_card("1", Card.from_string("ten of hearts"))
    t1.add_card("2", Card.from_string("queen of hearts"))
    t1.add_card("3", Card.from_string("king of hearts"))  # omnibus
    t1.add_card("4", Card.from_string("king of hearts"))  # omnibus

    print("checking result")
    assert t1.calculate_score() == "2"
    print("all ok!")

    print("-" * 10)
    print("creating test turn 2")
    t2 = Turn(4)

    print("setting trump")
    t2.set_trump(Card.from_string("two of clubs"))

    print("adding cards")
    t2.add_card("1", Card.from_string("ten of hearts"))
    t2.add_card("2", Card.from_string("queen of hearts"))
    t2.add_card("3", Card.from_string("king of hearts"))
    t2.add_card("4", Card.from_string("two of clubs"))  # trump card

    print("checking result")
    assert t2.calculate_score() == "4"
    print("all ok!")

    print("creating test turn 3")
    t3 = Turn(5)

    print("setting trump")
    t3.set_trump(Card.from_string("two of clubs"))

    print("adding cards")
    t3.add_card("1", Card.from_string("ten of hearts"))
    t3.add_card("2", Card.from_string("ten of hearts"))
    t3.add_card("3", Card.from_string("king of diamonds"))  # omnibus
    t3.add_card("4", Card.from_string("king of diamonds"))  # omnibus
    t3.add_card("5", Card.from_string("king of spades"))  # omnibus

    print("checking result")

    assert t3.calculate_score() == "5"
    print("all ok!")
