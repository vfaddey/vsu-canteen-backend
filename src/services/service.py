from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database.database import Base


class BaseService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, obj: Base):
        try:
            self._session.add(obj)
            await self._session.commit()
            await self._session.refresh(obj)
            return obj
        except IntegrityError as e:
            await self._session.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

    async def get_all(self):
        raise NotImplemented

    async def get(self, **kwargs):
        raise NotImplemented

    async def get_by_id(self, id: int):
        raise NotImplemented

    async def delete_by_id(self, id: int):
        raise NotImplemented