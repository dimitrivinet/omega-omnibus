# pylint: disable = missing-function-docstring

from collections import deque
from pathlib import Path

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


def test_empty_file(tmp_path: Path):
    storage_path = tmp_path / "games.pickle"
    storage_path_fake = tmp_path / "games_fake.pickle"

    p = PickleStorage(storage_path=storage_path, max_size=3)

    assert storage_path.exists()
    assert not storage_path_fake.exists()

    storage_path_fake.touch()
    p.storage_path = storage_path_fake

    p.load()

    assert p.games == deque(maxlen=3)
