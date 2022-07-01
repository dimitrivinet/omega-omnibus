import pickle

from omega_omnibus.config import cfg


def pre_init() -> None:
    """This function is called before the server starts."""

    # create game storage file if it doesn't exist and fill with dummy value
    if not cfg.GAMES_STORAGE_PATH.exists():
        with open(cfg.GAMES_STORAGE_PATH, "wb") as f:
            pickle.dump([], f)
