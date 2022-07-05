from typing import Optional

from fastapi import APIRouter, HTTPException, status

from ...global_instances import games_store

router = APIRouter(prefix="/play")


@router.get("{game_id}/players")
async def list_players(game_id: str):
    """List players."""

    return games_store()[game_id].players


@router.put("{game_id}/add_player/{player_name}")
async def add_player(game_id: str, player_name: str, save: Optional[bool] = True):
    """Add a player to the game."""

    game = games_store()[game_id]

    try:
        pid = game.add_player(player_name)
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from None

    if save:
        games_store().save()

    return pid


@router.post("{game_id}/freeze")
async def freeze_game(game_id: str, save: Optional[bool] = True):
    """Freeze the game."""

    game = games_store()[game_id]

    try:
        game.freeze_players()
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from None

    if save:
        games_store().save()

    return "success"
