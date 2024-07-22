from sqlalchemy.ext.asyncio import AsyncSession

from src.core.repository import AsyncSqlRepository
from src.users.api.database import Users


class UsersRepository(AsyncSqlRepository[Users]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
