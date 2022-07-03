from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from fastapi_utils.enums import StrEnum

from omega_omnibus.game.game_manager import GameManager

from ...game_storage import AlreadyExistsError
from ...global_instances import games_store

router = APIRouter()


class OnFullEnum(StrEnum):
    """Action to take when game storage is full."""

    DELETE = "delete"
    ERROR = "error"


@router.get("/games")
async def get_game_ids() -> List[str]:
    """Get stored game ids."""

    return games_store().keys()


@router.put("/games", status_code=status.HTTP_201_CREATED)
async def create_new_game(
    game_id: Optional[str] = None,
    on_full: OnFullEnum = OnFullEnum.DELETE,  # type: ignore
    # mypy throws error here ^ for no apparent reason
) -> str:
    """Create game and return its id."""

    new_game = GameManager()
    _games_store = games_store()

    try:
        created_id = _games_store.add_game(
            new_game, game_id=game_id, on_full=on_full.value
        )
    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Storage full."
        ) from None
    except AlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Already exists."
        ) from None

    _games_store.save()

    return created_id


@router.delete("/games")
async def delete_game(game_id: str):
    """Delete game by id."""

    try:
        del games_store()[game_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No such game: {game_id}"
        ) from None


@router.post("/games/save")
async def save_games():
    """Save games to storage."""

    games_store().save()
