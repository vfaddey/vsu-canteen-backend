from datetime import datetime

from pydantic import BaseModel

from src.dishes.schemas import DishSchema


class OrderCreate(BaseModel):
    dishes_ids: list[int]

class OrderUpdate(BaseModel):
    status: str

class OrderResponse(BaseModel):
    id: int
    dishes: list[DishSchema]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True