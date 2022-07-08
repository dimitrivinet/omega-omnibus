# pylint: disable = missing-function-docstring

from pathlib import Path

from pytest import MonkeyPatch

from omega_omnibus.game.game_manager import GameManager
from omega_omnibus.server import app
from omega_omnibus.server.game_storage.pickle_storage import PickleStorage
from omega_omnibus.server.global_instances import games_store


def test_startup(tmp_path: Path, monkeypatch: MonkeyPatch):
    storage_path = tmp_path / "games.pickle"

    setup_s = PickleStorage(storage_path, max_size=3)

    g1 = setup_s.add_game(GameManager())
    g2 = setup_s.add_game(GameManager())

    setup_s.save()

    monkeypatch.setenv("OO_GAMES_STORAGE_TYPE", "pickle")
    monkeypatch.setenv("OO_GAMES_STORAGE_PATH", str(storage_path))
    monkeypatch.setenv("OO_MAX_SAVED_GAMES", str(3))

    app.startup()
    s = games_store()

    assert len(s.keys()) == 2
    assert g1 in s
    assert g2 in s
