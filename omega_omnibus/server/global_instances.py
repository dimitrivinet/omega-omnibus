from omega_omnibus.config import cfg

from . import game_storage

games_store = game_storage.GameStorage(cfg.GAMES_STORAGE_PATH, cfg.MAX_SAVED_GAMES)
games_store.load()
