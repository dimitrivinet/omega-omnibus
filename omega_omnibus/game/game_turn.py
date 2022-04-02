"""Onmibus game turn (where each player plays a card once, clockwise).
First player determines the preferred card suit.
"""

from omega_omnibus.game.cards import Card


class Turn:
    """Represents a turn of Omnibus. Gets the trump card, the cards played
    during the turn, and calculates the points for each player."""

    num_players: int

    _dict: dict

    trump: Card

    def __init__(self, num_players: int):
        """Creates an empty turn. Must set trump card and add cards
        one by one."""

        self.num_players = num_players

        self._dict = {}

    def set_trump(self, trump: Card):
        """Set trump card for the turn."""

    def add_card(self, player_id: str, card: Card):
        """Add new card to turn."""

    def calculate_score(self):
        """Calculates turn score and returns winning player ID."""

    def _check_round_over(self):
        """Checks if everything was set properly for calculating score."""
