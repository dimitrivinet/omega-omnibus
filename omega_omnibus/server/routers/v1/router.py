from fastapi import APIRouter

from . import game, storage

router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(storage.router)
router.include_router(game.router)
