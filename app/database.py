import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from sqlalchemy import func, NullPool


# подумать, как сделать поумнее, возможно пронаследоваться от BaseSettings, как сделал нижк, пока итак работает
if settings.MODE == 'TEST':
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {'poolclass': NullPool, 'echo': True}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {'echo': True}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

# class Database(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str
#
#     class Config:
#         env_prefix = 'TEST_DB_' if os.getenv('MODE') else 'DB_'
#         case_sensitive = False
