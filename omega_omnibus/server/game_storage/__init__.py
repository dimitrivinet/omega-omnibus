from dataclasses import dataclass
from typing import List, Optional, Protocol

from omega_omnibus.game.game_manager import GameManager


class AlreadyExistsError(Exception):
    """Exception for when a game already exists in storage."""


@dataclass
class StoredGame:
    """Representation of a game in storage."""

    id: str
    manager: GameManager


class GameStorage(Protocol):
    """Storage manager for storing new and past games."""

    def load(self):
        """Load games."""
        ...

    def save(self):
        """Saves games to file."""
        ...

    def keys(self) -> List[str]:
        """Get all game ids."""
        ...

    def values(self) -> List[GameManager]:
        """Get all games."""
        ...

    def __contains__(self, key: str) -> bool:
        """Check if a game exists."""
        ...

    def __getitem__(self, key: str) -> GameManager:
        """Get a game by its id."""
        ...

    def add_game(
        self, value: GameManager, game_id: Optional[str] = None, on_full="delete"
    ) -> str:
        """Add a new game and returns its created id.

        on_full (str): Action to take when game list is full.
            - "delete": Delete oldest game to make space.
            - "error": Raise an error.
        """
        ...

    def __delitem__(self, key: str) -> None:
        """Delete a game."""
        ...
