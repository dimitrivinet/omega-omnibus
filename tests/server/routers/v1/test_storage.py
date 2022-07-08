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

    response = test_client.put(
        "/v1/games", params={"game_id": "test/test_2", "on_full": "delete"}
    )
    assert response.status_code == 201
    assert response.json() == r"test%2Ftest_2"


def test_get_game_info(test_client: TestClient):
    response = test_client.get("/v1/games/not-a-game")

    assert response.status_code == 404

    test_client.put("/v1/games", params={"game_id": "test_1"})

    response = test_client.get("/v1/games/test_1")

    assert response.status_code == 200


def test_delete_game(test_client: TestClient):
    test_client.put("/v1/games", params={"game_id": "test_1"})

    test_client.put("/v1/games", params={"game_id": "test_2"})

    response = test_client.get("/v1/games")
    assert response.status_code == 200
    assert response.json() == ["test_2", "test_1"]

    response = test_client.delete("/v1/games/test_1")
    assert response.status_code == 200

    response = test_client.delete("/v1/games/not-a-game")
    assert response.status_code == 404
    assert response.json() == {"detail": "No such game: not-a-game"}

    response = test_client.get("/v1/games")
    assert response.status_code == 200
    assert response.json() == ["test_2"]


def test_save_game(test_client: TestClient):
    response = test_client.post("/v1/games/save")
    assert response.status_code == 200
