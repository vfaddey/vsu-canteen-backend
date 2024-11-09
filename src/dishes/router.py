from fastapi import HTTPException

from fastapi import APIRouter
from fastapi.params import Depends

from src.dishes.models import Dish
from src.dishes.schemas import DishSchema, DishCreate
from src.services.dependencies import get_services
from src.services.general import Services

router = APIRouter(prefix='/dishes', tags=['dishes'])


@router.post('', response_model=DishSchema)
async def create_dish(add_dish: DishCreate,
                      services: Services = Depends(get_services)):
    dish = Dish(**add_dish.dict())
    inserted_dish = await services.dish_service.add(dish)
    return DishSchema.from_orm(inserted_dish)


@router.get('', response_model=list[DishSchema])
async def get_all_dishes(services: Services = Depends(get_services)):
    dishes = await services.dish_service.get_all()
    return [DishSchema.from_orm(dish) for dish in dishes]


@router.delete('/{dish_id}')
async def delete_dishes(dish_id: int,
                        services: Services = Depends(get_services)):
    result = await services.dish_service.delete_by_id(dish_id)
    if result:
        return {'status': 'ok'}
    raise HTTPException(status_code=404)