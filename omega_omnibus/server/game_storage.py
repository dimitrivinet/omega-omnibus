import pickle
import uuid
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, List

from omega_omnibus.game.game_manager import GameManager


@dataclass
class StoredGame:
    """Representation of a game in storage."""

    id: str
    manager: GameManager


class GameStorage:
    """Storage manager for storing new and past games."""

    storage_path: Path
    max_size: int

    games: Deque[StoredGame]

    def __init__(self, storage_path: Path, max_size: int = 10):
        self.storage_path = storage_path
        self.max_size = max_size

        self.games = deque(maxlen=max_size)

    def load(self):
        """Loads games from file."""

        with open(self.storage_path, "rb") as f:
            games = pickle.load(f)

        for game in games:
            self.games.appendleft(game)

    def save(self):
        """Saves games to file."""

        with open(self.storage_path, "wb") as f:
            pickle.dump(self.games, f)

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

    def add_game(self, value: GameManager, on_full="delete") -> str:
        """Add a new game and returns its created id.

        on_full (str): Action to take when game list is full.
            - "delete": Delete oldest game to make space.
            - "error": Raise an error.
        """

        if len(self.games) == self.max_size and on_full == "error":
            raise RuntimeError("Game list is full.")

        key = str(uuid.uuid4())
        self.games.appendleft(StoredGame(key, value))

        return key

    def __delitem__(self, key: str) -> None:
        """Delete a game."""

        for game in self.games:
            if game.id == key:
                self.games.remove(game)
                break

        raise KeyError(f"Game {key} not found.")
