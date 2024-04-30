import pytest  # isort:skip
from httpx import AsyncClient  # isort:skip
from new_app.main import (  # isort:skip # noqa
    Base,
    app,
    get_async_session,
)
from new_app.models import (  # isort:skip # noqa
    CookBook,
)
from sqlalchemy.ext.asyncio import (  # isort:skip
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(DATABASE_URL, echo=True)
test_async_session = async_sessionmaker(
    test_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
Base.metadata.bind = test_engine


async def override_get_async_session():
    async with test_async_session() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.mark.asyncio
async def test_add_dish():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    request_data = {
        "name_dish": "Test",
        "cooking_time": 45,
        "number_of_views": 0,
        "list_of_ingredients": "list",
        "description": "delicious",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/cookbook", json=request_data)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_dish():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/cookbook")
        assert response.status_code == 200
        assert response.json()[0]["name_dish"] == "Test"
        assert len(response.json()) == 1

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
