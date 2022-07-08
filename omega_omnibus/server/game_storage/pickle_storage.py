import pickle
from collections import deque
from pathlib import Path
from typing import Deque

from .game_storage import GameStorage, StoredGame


class PickleStorage(GameStorage):
    """Storage manager using pickle."""

    storage_path: Path

    def __init__(self, storage_path: Path, max_size: int = 10):
        super().__init__(max_size=max_size)

        self.storage_path = storage_path

        if not self.storage_path.exists():
            with open(self.storage_path, "wb") as f:
                pickle.dump(self.games, f)

    def load(self):
        """Load games from file."""

        with open(self.storage_path, "rb") as f:
            try:
                games = pickle.load(f)
            except EOFError:
                games = []

            if not isinstance(games, deque):
                games: Deque[StoredGame] = deque(maxlen=self.max_size)

        for game in games:
            self.games.appendleft(game)

        self.save()

    def save(self):
        """Save games to file."""

        with open(self.storage_path, "wb") as f:
            pickle.dump(self.games, f)
