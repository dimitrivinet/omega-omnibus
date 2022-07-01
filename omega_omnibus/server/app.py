from fastapi import FastAPI

from . import pre_init

pre_init.pre_init()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
