from fastapi import APIRouter, HTTPException
from fastapi import Depends

from src.orders.models import Order
from src.orders.schemas import OrderResponse, OrderCreate
from src.services.dependencies import get_services
from src.services.general import Services

router = APIRouter(prefix='/orders', tags=['orders'])


@router.post('', response_model=OrderResponse)
async def make_order(add_order: OrderCreate,
                     services: Services = Depends(get_services)):
    if not len(add_order.dishes_ids):
        raise HTTPException(400, detail='Нужно добавить хотя бы одно блюдо')
    order = Order()
    dishes = await services.dish_service.get_by_ids(add_order.dishes_ids)
    if len(dishes) != len(add_order.dishes_ids):
        raise HTTPException(400, detail='Какого-то блюда не существует')
    order.dishes.extend(dishes)
    inserted_order = await services.order_service.add(order)
    return OrderResponse.from_orm(inserted_order)


@router.get('', response_model=list[OrderResponse])
async def get_orders(services: Services = Depends(get_services)):
    return await services.order_service.get_all()


@router.delete('/{order_id}')
async def delete_order(order_id: int,
                       services: Services = Depends(get_services)):
    result = await services.order_service.delete_by_id(order_id)
    if result:
        return {'status': 'ok'}
    raise HTTPException(status_code=400)