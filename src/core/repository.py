from typing import Generic, Sequence, Type, TypeVar, final, get_args

from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import Base

T = TypeVar("T", bound=Base)


class AsyncSqlRepository(Generic[T]):
    def __init__(self, session: AsyncSession):
        self._session = session
        self._model = self.__get_model()

    def __get_model(self) -> Type[T]:
        return get_args(self.__orig_bases__[0])[0]  # type: ignore

    @final
    async def get_all(self) -> Sequence[T]:
        stmt = select(self._model)
        result = await self._session.scalars(stmt)
        return result.all()

    @final
    async def get_by_pk(self, pk: str) -> T:
        stmt = select(self._model).where(inspect(self._model).primary_key[0] == pk)
        result = await self._session.scalars(stmt)
        return result.first()
