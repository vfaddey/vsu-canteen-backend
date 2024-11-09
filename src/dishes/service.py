from fastapi import HTTPException
from starlette import status

from sqlalchemy import select, delete

from src.services.service import BaseService
from src.dishes.models import Dish


class DishService(BaseService):
    async def get_by_id(self, id: int):
        result = await self._session.execute(select(Dish).where(Dish.id == id))
        dish = result.scalars().first()
        if dish is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Dish with id {id} not found")
        return dish

    async def get_all(self):
        result = await self._session.execute(select(Dish))
        return result.scalars().all()

    async def delete_by_id(self, id: int):
        result = await self._session.execute(delete(Dish).where(Dish.id == id))
        if result.rowcount == 0:
            raise HTTPException(404, detail='No dish with such id')
        await self._session.commit()
        return result

    async def get_by_ids(self, ids: list[int]):
        result = await self._session.execute(select(Dish).where(Dish.id.in_(ids)))
        return result.scalars().all()