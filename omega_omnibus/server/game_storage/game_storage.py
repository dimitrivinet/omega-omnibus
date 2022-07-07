import uuid
from collections import deque
from dataclasses import dataclass
from typing import Deque, List, Optional

from omega_omnibus.game.game_manager import GameManager


class AlreadyExistsError(Exception):
    """Exception for when a game already exists in storage."""


@dataclass
class StoredGame:
    """Representation of a game in storage."""

    id: str
    manager: GameManager


class GameStorage:
    """Storage manager base implementation."""

    max_size: int

    games: Deque[StoredGame]

    def __init__(self, max_size: int = 10):
        self.max_size = max_size

        self.games = deque(maxlen=self.max_size)

    def load(self):
        """Load games."""

    def save(self):
        """Save games."""

    def keys(self) -> List[str]:
        """Get all game ids."""

        return [game.id for game in self.games]

    def values(self) -> List[GameManager]:
        """Get all games."""

        return [game.manager for game in self.games]

    def __contains__(self, key: str) -> bool:
        """Check if a game exists."""

        return key in self.keys()  # noqa: SIM118

    def __getitem__(self, key: str) -> GameManager:
        """Get a game by its id."""

        for game in self.games:
            if game.id == key:
                return game.manager

        raise KeyError(f"Game {key} not found.")

    def add_game(
        self, value: GameManager, game_id: Optional[str] = None, on_full="delete"
    ) -> str:
        """Add a new game and returns its created id.

        on_full (str): Action to take when game list is full.
            - "delete": Delete oldest game to make space.
            - "error": Raise an error.
        """

        if len(self.games) == self.max_size and on_full == "error":
            raise RuntimeError("Game storage is full.")

        if game_id is None:
            key = str(uuid.uuid4())
        else:
            if game_id in self:
                raise AlreadyExistsError("game_id")

            key = game_id

        self.games.appendleft(StoredGame(key, value))

        return key

    def __delitem__(self, key: str) -> None:
        """Delete a game."""

        for game in self.games:
            if game.id == key:
                self.games.remove(game)
                return

        raise KeyError(f"Game {key} not found.")
