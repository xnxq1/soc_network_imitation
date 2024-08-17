import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config import settings


if os.environ.get('MODE') == 'TEST':
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {'poolclass': NullPool}
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        future=True,
        **DATABASE_PARAMS,
    )
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,
        pool_size=10,
        future=True,
        **DATABASE_PARAMS,
    )

async_session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


