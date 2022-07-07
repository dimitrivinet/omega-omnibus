from collections import deque

import pytest

from omega_omnibus.game.game_manager import GameManager
from omega_omnibus.server.game_storage.game_storage import (
    AlreadyExistsError,
    GameStorage,
    StoredGame,
)

# pylint: disable = missing-function-docstring


def test_create_game_storage():
    s = GameStorage(max_size=3)

    assert s.games == deque(maxlen=3)
    assert s.max_size == 3


def test_game_storage_methods():
    s = GameStorage(max_size=3)

    k1 = s.add_game(GameManager())
    k2 = s.add_game(GameManager())
    k3 = s.add_game(GameManager())

    assert len(s.games) == 3
    assert all([isinstance(game, StoredGame) for game in s.games])

    assert len(s.keys()) == 3
    assert s.keys() == [k3, k2, k1]

    assert len(s.values()) == 3
    assert all((isinstance(game, GameManager) for game in s.values()))

    assert all((k in s for k in [k1, k2, k3]))

    assert isinstance(s[k1], GameManager)
    assert s[k1] == s.values()[2]

    with pytest.raises(KeyError) as excinfo:
        _ = s["not-a-key"]
        assert "Game not-a-key not found." in excinfo.value

    with pytest.raises(RuntimeError) as excinfo:
        s.add_game(GameManager(), on_full="error")
        assert "Game storage is full." in excinfo.value

    s.add_game(GameManager(), game_id="test", on_full="delete")

    with pytest.raises(AlreadyExistsError) as excinfo:
        s.add_game(GameManager(), game_id="test", on_full="delete")
        assert "Game test already exists." in excinfo.value

    del s[k3]
    assert k3 not in s
    assert len(s.games) == 2
    assert len(s.keys()) == 2
    assert len(s.values()) == 2

    with pytest.raises(KeyError) as excinfo:
        del s["not-a-key"]
        assert "Game not-a-key not found." in excinfo.value
