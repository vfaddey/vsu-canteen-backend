from fastapi import HTTPException

from sqlalchemy import select, delete

from src.services.service import BaseService
from src.orders.models import Order


class OrderService(BaseService):
    async def get_by_id(self, id: int):
        result = await self._session.execute(select(Order).where(Order.id == id))
        order = result.scalars().first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    async def get_all(self):
        result = await self._session.execute(select(Order))
        orders = result.unique().scalars().all()
        return orders

    async def delete_by_id(self, id: int):
        result = await self._session.execute(delete(Order).where(Order.id == id))
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Order not found")
        return result