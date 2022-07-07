# from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

# from decouple import Choices, config  # type: ignore
from pydantic import BaseSettings, validator


class Config(BaseSettings):
    """Application configuration."""

    # pylint: disable = no-self-use, no-self-argument

    GAMES_STORAGE_TYPE: str = "memory"
    GAMES_STORAGE_PATH: Path = Path("games.pickle")
    MAX_SAVED_GAMES: int = 10

    @validator("GAMES_STORAGE_TYPE")
    def must_be_valid_type(cls, v: str) -> str:
        """Validate that the storage type is valid."""

        valid_types = ["memory", "pickle"]

        if v not in valid_types:
            raise ValueError(
                f"Invalid storage type: {v}. Must be one of: ({', '.join(valid_types)})"
            )

        return v

    @validator("GAMES_STORAGE_PATH")
    def resolve_path(cls, v: Path) -> Path:
        """Resolve path."""

        return v.resolve()

    class Config:
        """Inner config class for pydantic BaseSettings."""

        env_prefix = "OO_"


@lru_cache
def cfg() -> Config:
    """Get the global configuration."""

    return Config()
