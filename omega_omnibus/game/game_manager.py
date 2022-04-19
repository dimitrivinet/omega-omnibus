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

    player_order: list

    def __init__(self):
        self.players = {}
        self.rounds = []
        self.current_round_index = -1
        self.game_started = False

    def add_player(self, name):
        """Add player to game. Generates uuid corresponding to player.
        New players can't be added after game has started with start_game()."""

        if self.game_started:
            raise RuntimeError(
                " ".join(
                    (
                        "A player cannot be added while the game is running.",
                        f"(tried to add player {repr(name)})",
                    )
                )
            )

        new_player = Player(name)
        self.players[new_player.id] = Player(name)

        return new_player.id

    def _create_current_round(self, first_player: str):
        """Create current round."""

        if len(self.rounds) != self.current_round_index:  # if round already exists
            raise RuntimeError("Round already created.")

        new_round = game_round.Round(
            num_turns=ROUND_ORDER[self.current_round_index],
            player_ids=list(self.players.keys()),
            first_player=first_player,
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

        if len(self.players) < 2:
            raise RuntimeError("Cannot play with less than 2 players.")

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
        self._create_current_round(first_player=first_player)

    def next_round(self):
        """Creates next round. Game must be started with start_game().
        Throws error if current round was not finished."""

        if not self.game_started:
            raise RuntimeError("Game is not started!")

        if not self.rounds[self.current_round_index].over:
            raise RuntimeError("Current round is not over!")

        self.current_round_index += 1

        self._rotate_player_order()
        self._create_current_round(self.player_order[0])

    def set_trump(self, trump: cards.Card):
        """Set trump card for the current turn."""

        self.rounds[self.current_round_index].set_trump(trump)

    def add_card(self, card: cards.Card):
        """Add new card to current turn."""

        self.rounds[self.current_round_index].add_card(card)

    def calculate_scores(self):
        """Calculates current round scores and updates player scores."""

        # scores = self.rounds[self.current_round_index].calculate_scores()
