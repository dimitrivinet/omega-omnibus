from dataclasses import dataclass
from pathlib import Path

from decouple import config


@dataclass
class Config:
    """Command line configuration."""

    # pylint: disable=invalid-name

    # Path to the game storage file.
    # Absolute or relative to where you call the server.
    GAMES_STORAGE_PATH: Path = config(
        "OO_GAMES_STORAGE_PATH",
        cast=lambda x: Path(x).resolve(),
        default="games.pickle",
    )

    # Maximum number of games to store.
    MAX_SAVED_GAMES: int = config("OO_MAX_SAVED_GAMES", cast=int, default=10)


cfg = Config()
print(cfg)
