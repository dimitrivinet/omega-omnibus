# pylint: disable = missing-function-docstring

import pytest
from fastapi.testclient import TestClient
from pytest import MonkeyPatch

from omega_omnibus.server.app import app, startup
from omega_omnibus.server.config import cfg
from omega_omnibus.server.global_instances import games_store


@pytest.fixture
def test_client(_reset_lru_caches, monkeypatch: MonkeyPatch) -> TestClient:
    monkeypatch.setenv("OO_GAMES_STORAGE_TYPE", "memory")
    monkeypatch.setenv("OO_MAX_SAVED_GAMES", str(3))

    client = TestClient(app)
    startup()

    return client


@pytest.fixture(name="_reset_lru_caches")
def reset_lru_caches():
    games_store.cache_clear()
    cfg.cache_clear()
