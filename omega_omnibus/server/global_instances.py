from functools import lru_cache

from .config import cfg
from .game_storage import pickle_storage
from .game_storage.game_storage import GameStorage


@lru_cache
def games_store() -> GameStorage:
    """Get the global game store. Returns the same instance every time."""

    _games_store: GameStorage
    config = cfg()

    if config.GAMES_STORAGE_TYPE == "pickle":
        _games_store = pickle_storage.PickleStorage(
            config.GAMES_STORAGE_PATH, config.MAX_SAVED_GAMES
        )
    else:
        _games_store = GameStorage(config.MAX_SAVED_GAMES)

    return _games_store
