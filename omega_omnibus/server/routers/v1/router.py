from fastapi import APIRouter

from . import storage

router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(storage.router)
