from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DSN = 'postgresql+asyncpg://postgres:postgres@localhost:5432/aiohttp_db'
engine = create_async_engine(DSN)

Session = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)
Base = declarative_base()


class Ad(Base):
    __tablename__ = "Ad"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)
