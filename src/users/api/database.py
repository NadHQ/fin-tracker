from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class Users(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
