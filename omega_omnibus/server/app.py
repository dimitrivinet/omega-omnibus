from fastapi import FastAPI

from . import pre_init
from .routers.v1 import router as v1router

tags_metadata = [
    {
        "name": "v2",
        "description": "API v2",
    },
    {
        "name": "v1",
        "description": "API v1",
    },
]


pre_init.pre_init()
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(v1router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
