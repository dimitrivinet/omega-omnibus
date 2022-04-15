from typing import Dict, List

from omega_omnibus.game import cards


class Round:
    """Omnibus game round."""

    num_turns: int
    player_ids: List[str]
    first_player: str

    def __init__(self, num_turns: int, player_ids: List[str], first_player: str):
        self.num_turns = num_turns
        self.player_ids = player_ids
        self.first_player = first_player

    def set_trump(self, trump: cards.Card):
        """Set trump card for the current turn."""

    def add_card(self, card: cards.Card):
        """Add new card to current turn."""

    def calculate_scores(self) -> Dict[str, int]:
        """Calculates current round scores and updates player scores."""

    @property
    def over(self) -> bool:
        """True if round is over, else False."""

        # ! TODO
        return False
