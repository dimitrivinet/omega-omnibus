# pylint: disable = missing-function-docstring

from pathlib import Path

import pytest
from pydantic import ValidationError
from pytest import MonkeyPatch

from omega_omnibus.server.config import Config, cfg


def test_default_config(_reset_lru_caches):
    c = Config()

    assert c.GAMES_STORAGE_TYPE == "memory"
    assert c.GAMES_STORAGE_PATH == Path("games.pickle").resolve()
    assert c.MAX_SAVED_GAMES == 10


def test_pickle_storage_config():
    c = Config(
        GAMES_STORAGE_TYPE="pickle",
        GAMES_STORAGE_PATH="games.pickle",
        MAX_SAVED_GAMES=3,
    )

    assert c.GAMES_STORAGE_TYPE == "pickle"
    assert c.GAMES_STORAGE_PATH == Path("games.pickle").resolve()
    assert isinstance(c.GAMES_STORAGE_PATH, Path)
    assert c.MAX_SAVED_GAMES == 3


def test_manual_envvars_config(_reset_lru_caches, monkeypatch: MonkeyPatch):
    monkeypatch.setenv("OO_GAMES_STORAGE_TYPE", "memory")
    monkeypatch.setenv("OO_GAMES_STORAGE_PATH", "games.pickle")
    monkeypatch.setenv("OO_MAX_SAVED_GAMES", str(3))

    config = cfg()

    assert config.GAMES_STORAGE_TYPE == "memory"
    assert config.GAMES_STORAGE_PATH == Path("games.pickle").resolve()
    assert config.MAX_SAVED_GAMES == 3


def test_invalid_values():
    with pytest.raises(ValidationError) as excinfo:
        _ = Config(GAMES_STORAGE_TYPE="invalid")
        assert "Invalid storage type" in excinfo
