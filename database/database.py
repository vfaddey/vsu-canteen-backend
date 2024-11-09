from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import DB_URL

Base = declarative_base()

engine = create_async_engine(DB_URL, echo=False)
AsyncSessionFactory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)