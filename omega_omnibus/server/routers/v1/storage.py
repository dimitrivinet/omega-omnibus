import urllib.parse
from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from fastapi_utils.enums import StrEnum

from omega_omnibus.game.game_manager import GameManager

from ...game_storage.game_storage import AlreadyExistsError
from ...global_instances import games_store

router = APIRouter(prefix="/games")


class OnFullEnum(StrEnum):
    """Action to take when game storage is full."""

    DELETE = "delete"
    ERROR = "error"


@router.get("")
async def get_game_ids() -> List[str]:
    """Get stored game ids."""

    return games_store().keys()


@router.put("", status_code=status.HTTP_201_CREATED)
async def create_new_game(
    game_id: Optional[str] = None,
    on_full: OnFullEnum = OnFullEnum.DELETE,  # type: ignore
    # mypy throws error here ^ for no apparent reason
    save: Optional[bool] = True,
) -> str:
    """Create game and return its id."""

    new_game = GameManager()
    _games_store = games_store()

    if game_id is not None:
        game_id = urllib.parse.quote_plus(game_id)

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

    if save:
        _games_store.save()

    return created_id


@router.get("/{game_id}")
async def get_game_info(game_id: str):
    """Get game info."""

    try:
        ret = games_store()[game_id].dict()
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        ) from None

    return ret


@router.delete("/{game_id}")
async def delete_game(game_id: str, save: Optional[bool] = True):
    """Delete game by id."""

    try:
        del games_store()[game_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No such game: {game_id}"
        ) from None

    if save:
        games_store().save()


@router.post("/save")
async def save_games():
    """Save games to storage."""

    games_store().save()
