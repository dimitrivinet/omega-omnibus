# pylint: disable = missing-function-docstring

from collections import deque

from omega_omnibus.game.game_manager import GameManager
from omega_omnibus.server.game_storage.pickle_storage import PickleStorage


def test_pickle_storage(tmp_path):
    storage_path = tmp_path / "games.pickle"

    p = PickleStorage(storage_path=storage_path, max_size=3)

    assert p.max_size == 3
    assert p.games == deque(maxlen=3)
    assert p.storage_path == storage_path

    g = GameManager()
    gid1 = p.add_game(g)
    p.save()

    other_p = PickleStorage(storage_path=storage_path, max_size=3)
    other_p.load()

    assert len(other_p.games) == 1

    # can't test for manager equality because they have different memory addresses
    for game in other_p.games:
        assert game.id == gid1
        assert game.manager.dict() == g.dict()
