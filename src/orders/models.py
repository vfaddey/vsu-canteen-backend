import enum
from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, Table
from sqlalchemy.orm import relationship

from database.database import Base


class OrderStatus(enum.Enum):
    PENDING = 'pending'
    PREPARING = 'preparing'
    READY = 'ready'
    CANCELLED = 'cancelled'


dishes_orders = Table(
    'dishes_orders',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id', ondelete="CASCADE"), primary_key=True),
    Column('dish_id', Integer, ForeignKey('dishes.id', ondelete="CASCADE"), primary_key=True),
)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

    dishes = relationship('Dish', secondary=dishes_orders, lazy='joined', cascade='all, delete')

