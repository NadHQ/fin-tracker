from typing import List

from fastapi import APIRouter
from starlette import status

from src.core.database import AsyncSessionMaker
from src.users.api.serializers.users import UsersSerializer
from src.users.api.uow import UsersUow

v1_router = APIRouter(prefix="/users", tags=["Users Endpoints"])


@v1_router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_users() -> List[UsersSerializer]:
    async with UsersUow(session_maker=AsyncSessionMaker) as unit_of_work:
        result = await unit_of_work.user_repository.get_all()
        return result


@v1_router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_user_by_pk(uuid: str) -> UsersSerializer:
    async with UsersUow(session_maker=AsyncSessionMaker) as unit_of_work:
        result = await unit_of_work.user_repository.get_by_pk(uuid)
        return result
