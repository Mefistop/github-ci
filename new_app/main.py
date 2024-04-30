from typing import List

from fastapi import Depends, FastAPI, Path
from fastapi.exceptions import HTTPException
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .database import async_session, engine
from .models import Base, CookBook
from .schemas import CookBookBrieflyOut, CookBookIn, CookBookOut

app = FastAPI()
id_path = Path(..., title="id of dish")


async def get_async_session():
    async with async_session() as session:
        yield session


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await async_session.close()
    await engine.dispose()


@app.post("/cookbook", response_model=CookBookOut)
async def add_new_dish(
    dish: CookBookIn, session: AsyncSession = Depends(get_async_session)
) -> CookBookOut:
    new_dish = CookBook(**dish.dict())
    session.add(new_dish)
    await session.commit()
    return CookBookOut.from_orm(new_dish)


@app.get("/cookbook", response_model=List[CookBookBrieflyOut])
async def get_all_dishes(
    session: AsyncSession = Depends(get_async_session),
) -> List[CookBookBrieflyOut]:
    res = await session.execute(
        select(
            CookBook.name_dish,
            CookBook.cooking_time,
            CookBook.number_of_views,
        ).order_by(
            CookBook.number_of_views.desc(),
            CookBook.cooking_time,
        )
    )
    return [CookBookBrieflyOut.from_orm(row) for row in res.all()]


@app.get("/cookbook/{id}", response_model=CookBookOut)
async def get_dish(
    id: int = id_path, session: AsyncSession = Depends(get_async_session)
) -> CookBookOut:
    res = await session.execute(select(CookBook).where(CookBook.id == id))
    dish = res.scalar()
    if dish:
        query = (
            update(CookBook)
            .where(CookBook.id == id)
            .values(number_of_views=dish.number_of_views + 1)
        )
        await session.execute(query)
        await session.commit()
        return CookBookOut.from_orm(dish)
    else:

        raise HTTPException(status_code=404, detail="Dish not found")
