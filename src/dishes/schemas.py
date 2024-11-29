from pydantic import BaseModel


class DishCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    day: str
    category: str

class DishSchema(DishCreate):
    id: int

    class Config:
        from_attributes = True
