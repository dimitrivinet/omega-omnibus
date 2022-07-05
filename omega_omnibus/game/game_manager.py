"""
Player dict tempalte:
{
    "player_id (uuid)": {
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

from __future__ import annotations

import random
import uuid
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Union

from omega_omnibus.game import cards, game_round

# 1, 2, 3, ... 11, 12, 11, ..., 3, 2, 1
ROUND_ORDER = list(range(1, 12)) + list(range(12, 0, -1))


@dataclass
class Player:
    """Omnibus player."""

    id: str = field(init=False)
    name: str
    score: int = field(init=False)
    history: dict = field(init=False, repr=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())  # random id
        self.score = 0  # game score, starts at 0
        self.history = {**{round_index: [] for round_index in range(len(ROUND_ORDER))}}


class FPC(Enum):
    """First player choice method."""

    RANDOM = auto()
    FIRST_ADDED = auto()
    MANUAL = auto()

    @classmethod
    def to_enum(cls, fpc: Union[str, FPC]) -> FPC:
        """Convert a string or enum member to an enum member."""

        for member in cls:
            if fpc in [member, member.name]:
                return member

        raise ValueError("Choice not found in enum.")


class GameManager:
    """Manages the full game of Omnibus.

    Add players one by one with add_player(), then start the game with
    start_game() to begin the first round. Subsequent rounds can be started
    with next_round().
    """

    players: Dict[str, Player]
    rounds: List[game_round.Round]
    current_round_index: int
    game_started: bool
    _players_frozen: bool

    player_order: list

    def __init__(self):
        self.players = {}
        self.rounds = []
        self.current_round_index = -1
        self.game_started = False
        self._players_frozen = False

    def dict(self) -> dict:
        """Get dict representation of the game manager."""

        return {
            "players": [f"{p.name} ({p.id})" for p in self.players.values()],
            "rounds": self.rounds,
            "current_round_index": self.current_round_index,
            "game_started": self.game_started,
        }

    def add_player(self, name):
        """Add player to game. Generates uuid corresponding to player.
        New players can't be added after game has started with start_game()."""

        if self._players_frozen:
            raise RuntimeError(
                " ".join(
                    (
                        "A player cannot be added after players were frozen.",
                        f"(tried to add player {repr(name)})",
                    )
                )
            )

        new_player = Player(name)
        self.players[new_player.id] = Player(name)

        return new_player.id

    def freeze_players(self):
        """Freeze player order and ids."""

        if len(self.players) < 2:
            raise RuntimeError("Cannot play with less than 2 players.")

        if self._players_frozen:
            raise RuntimeError("Players are already frozen.")

        self._players_frozen = True

        self.player_order = list(self.players.keys()).copy()

    def _create_current_round(self):
        """Create current round."""

        if len(self.rounds) != self.current_round_index:  # if round already exists
            raise RuntimeError("Round already created.")

        new_round = game_round.Round(
            num_turns=ROUND_ORDER[self.current_round_index],
            player_order=self.player_order,
        )
        self.rounds.append(new_round)

    def _rotate_player_order(self):
        """Rotate player order list to get the play order of current turn."""

        if not hasattr(self, "player_order") or len(self.player_order) < 1:
            return

        self.player_order.append(self.player_order.pop(0))

    def start_game(
        self,
        /,
        first_player: str = "",
        first_player_choice: Union[FPC, str] = FPC.FIRST_ADDED,
    ):
        """Starts game."""

        if self.game_started:
            raise RuntimeError("Game already started.")

        if not self._players_frozen:
            raise RuntimeError("Players must be frozen before starting game.")

        fpc = FPC.to_enum(first_player_choice)

        if fpc == FPC.FIRST_ADDED:
            first_player = list(self.players.keys())[0]
        elif fpc == FPC.RANDOM:
            first_player = random.choice(list(self.players.keys()))  # type: ignore
        elif fpc == FPC.MANUAL and first_player not in self.players:
            raise RuntimeError(
                " ".join(
                    (
                        "Specified manual first player choice but",
                        "first player choice is not in players.",
                        f"(player choice: {repr(first_player)},"
                        f"players: {self.players.keys()})",
                    )
                )
            )

        self.player_order = list(self.players.keys())
        while self.player_order[0] != first_player:
            self._rotate_player_order()

        self.game_started = True
        self.current_round_index = 0
        self._create_current_round()

    def next_round(self):
        """Creates next round. Game must be started with start_game().
        Throws error if current round was not finished."""

        if not self.game_started:
            raise RuntimeError("Game is not started!")

        if self.over:
            return self.over

        if not self.rounds[self.current_round_index].over:
            raise RuntimeError("Current round is not over!")

        self.current_round_index += 1

        self._rotate_player_order()
        self._create_current_round()

        return self.over

    def next_turn(self):
        """Go to next turn."""

        self.rounds[self.current_round_index].next_turn()

    def set_trump(self, trump: cards.Card):
        """Set trump card for the current turn."""

        self.rounds[self.current_round_index].set_trump(trump)

    def add_card(self, card: cards.Card):
        """Add new card to current turn."""

        self.rounds[self.current_round_index].add_card(card)

    def calculate_score(self):
        """Calculates current round scores and updates player scores."""

        if not self.rounds[self.current_round_index].over:
            self.rounds[self.current_round_index].calculate_score()

        # scores = self.rounds[self.current_round_index].calculate_scores()

    @property
    def over(self):
        """Is game over."""

        return len(self.rounds) == 23 and all(r.over for r in self.rounds)


if __name__ == "__main__":  # pragma: no cover
    m = GameManager()

    while True:
        ret = input("Type player name to add (type 'd' for default, 'q' to quit): ")
        if ret == "q":
            break

        if ret in ["default", "d"]:
            m.add_player("dimitri")
            m.add_player("yann")
            m.add_player("leah")
            m.add_player("clement")
            m.add_player("vincent")
            break

        m.add_player(ret)

    print(f"Players: {', '.join([player.name for player in m.players.values()])}")

    m.freeze_players()
    m.start_game(first_player_choice="RANDOM")
    print("Game started.")
    print(m.rounds)
    print([m.players[p_id].name for p_id in m.player_order])
