from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from .shemas import Base
from core.models.items import Items


async def get_all_items(session: AsyncSession) -> list[Items]:
    statement = select(Items).order_by(Items.id)
    result: Result = await session.execute(statement)
    items = result.scalars().all()
    return list(items)


async def get_item(session: AsyncSession, item_id: int) -> Items | None:
    return await session.get(Items, item_id)


async def create_item(session: AsyncSession, item_in: Base) -> Items:
    item = Items(**item_in.model_dump())
    session.add(item)
    await session.commit()
    return item
