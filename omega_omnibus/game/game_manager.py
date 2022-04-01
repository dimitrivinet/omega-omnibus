"""
Player dict tempalte:
{
    "player_id (str: uuid)": {
        "name": name (str),
        "score": score (int),
        "history": {
            [
                {
                    "target_tricks": target (int),
                    "result": result (int),
                    "round_score": round_score (int)
                },
                ...
            ]
        }
    },
    ...
}
"""

# from omega_omnibus.game import game_round

ROUND_ORDER = list(range(12, 1, -1)) + list(range(1, 13))


class GameManager:
    """Manages the full game of Omnibus.

    Add players one by one with add_player(), then start the game with
    start_game() to begin the first round. Subsequent rounds can be started
    with next_round().
    """

    players: dict
    rounds: dict
    current_round_index: int
    game_started: bool

    def __init__(self):
        self.players = {}
        self.rounds = []
        self.current_round_index = 0
        self.game_started = False

    def add_player(self, name):
        """Add player to game. Generates uuid corresponding to player.
        New players can't be added after game has started with start_game()."""

    def start_game(self):
        """Starts game."""

    def next_round(self):
        """Creates next round. Game must be started with start_game()."""

    def set_trump(self):
        """Set trump card for the current round."""

    def add_card(self):
        """Add new card to current round."""

    def calculate_score(self):
        """Calculates current round score and updates scores."""
