import os

import pytest
from fastapi.testclient import TestClient

from omega_omnibus.server.app import app


@pytest.fixture(name="test_client")
def _fastapi_test_client() -> TestClient:
    os.environ["OO_GAMES_STORAGE_TYPE"] = "memory"
    os.environ["OO_MAX_SAVED_GAMES"] = str(3)

    client = TestClient(app)

    return client
