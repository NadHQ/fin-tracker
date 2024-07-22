from src.core.uow import BaseUow
from src.users.repository.users import UsersRepository


class UsersUow(BaseUow):
    user_repository: UsersRepository

    async def __aenter__(self):
        await super().__aenter__()

        self.user_repository = UsersRepository(self._session)

        return self
