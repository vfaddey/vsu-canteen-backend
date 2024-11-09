from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dependencies import get_session
from src.services.general import Services


async def get_services(session: AsyncSession = Depends(get_session)):
    return Services(session)