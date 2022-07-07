# pylint: disable = missing-function-docstring

from fastapi.testclient import TestClient


def test_list_players(test_client: TestClient):
    response = test_client.get("/v1/games")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_players(test_client: TestClient):
    response = test_client.get("/v1/games")

    assert response.status_code == 200
    assert response.json() == []

    response = test_client.put("/v1/games", params={"game_id": "test_1"})

    assert response.status_code == 201
    assert response.json() == "test_1"

    response = test_client.get("/v1/games")

    assert response.status_code == 200
    assert response.json() == ["test_1"]

    response = test_client.put("/v1/games", params={"game_id": "test_2"})
    response = test_client.put("/v1/games", params={"game_id": "test_3"})

    response = test_client.get("/v1/games")

    assert response.status_code == 200
    assert response.json() == ["test_3", "test_2", "test_1"]

    response = test_client.put("/v1/games", params={"game_id": "test_4"})

    assert response.status_code == 201
    assert response.json() == "test_4"

    response = test_client.get("/v1/games")

    assert response.status_code == 200
    assert response.json() == ["test_4", "test_3", "test_2"]

    response = test_client.put(
        "/v1/games", params={"game_id": "test_5", "on_full": "error"}
    )

    assert response.status_code == 409
    assert response.json() == {"detail": "Storage full."}

    response = test_client.put("/v1/games", params={"game_id": "test_4"})

    assert response.status_code == 409
    assert response.json() == {"detail": "Already exists."}
