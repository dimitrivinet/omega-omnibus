from omega_omnibus.game.cards import Card


class Round:
    """Represents a round of Omnibus. Gets the trump card, the cards played
    during the round, and calculates the points for each player."""

    num_players: int

    _dict: dict

    trump: Card

    def __init__(self, num_players: int):
        """Creates an empty round. Must set trump card and add cards
        one by one."""

        self.num_players = num_players

        self._dict = {}

    def set_trump(self, trump: Card):
        """Set trump card for the round."""

    def add_card(self, player_id: str, card: Card):
        """Add new card to round."""

    def calculate_score(self):
        """Calculates round score and returns winning player ID."""

    def _check_round_over(self):
        """Checks if everything was set properly for calculating score."""
