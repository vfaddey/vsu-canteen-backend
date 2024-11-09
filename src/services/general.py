from sqlalchemy.ext.asyncio import AsyncSession

from src.dishes.service import DishService
from src.orders.service import OrderService


class Services:
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.dish_service: DishService = DishService(self.__session)
        self.order_service: OrderService = OrderService(self.__session)