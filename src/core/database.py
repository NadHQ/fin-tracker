from decouple import config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = config("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
AsyncSessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
