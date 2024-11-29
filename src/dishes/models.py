from sqlalchemy import Column, Integer, String, Float

from database.database import Base


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, default='')
    price = Column(Float)
    category = Column(String, default='Вторые блюда')
    day = Column(String, default='Понедельник')
    image_url = Column(String, default='#')