from fastapi import FastAPI

from src.users.api.v1.users import v1_router

app = FastAPI()

app.include_router(v1_router)
