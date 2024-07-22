from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import AsyncSessionMaker


class AbstractBaseUow(ABC):
    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class BaseUow(AbstractBaseUow):
    def __init__(self, session_maker: AsyncSessionMaker):
        self._session_maker = session_maker
        self._session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self._session = self._session_maker()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                await self._session.commit()
            except SQLAlchemyError:
                await self._session.rollback()
                raise
        else:
            await self._session.rollback()
        await self._session.close()

    @property
    def session(self) -> AsyncSession:
        return self._session
