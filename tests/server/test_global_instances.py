import os

from omega_omnibus.server.config import cfg
from omega_omnibus.server.game_storage.game_storage import GameStorage
from omega_omnibus.server.game_storage.pickle_storage import PickleStorage
from omega_omnibus.server.global_instances import games_store


def test_memory_instance():
    os.environ["OO_GAMES_STORAGE_TYPE"] = "memory"

    gs1 = games_store()

    assert type(gs1) is GameStorage  # pylint: disable = unidiomatic-typecheck

    gs2 = games_store()

    assert gs1 is gs2
    assert gs1 == gs2

    cfg.cache_clear()
    games_store.cache_clear()

    os.environ["OO_GAMES_STORAGE_TYPE"] = "pickle"

    gs3 = games_store()

    assert type(gs3) is PickleStorage  # pylint: disable = unidiomatic-typecheck

    gs4 = games_store()

    assert gs3 is gs4
    assert gs3 == gs4
