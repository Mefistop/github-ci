# from httpx import AsyncClient
# import pytest
# from sqlalchemy.ext.asyncio import (  # isort:skip
#     AsyncSession,
#     async_sessionmaker,
#     create_async_engine,
# )
# from python_advanced.module_30_ci_linters.homework.new_app.main import Base
# from python_advanced.module_30_ci_linters.homework.new_app.main import
# get_async_session
# from python_advanced.module_30_ci_linters.homework.new_app.main import
# app
# from python_advanced.module_30_ci_linters.homework.new_app.models import
# CookBook
#
# DATABASE_URL = "sqlite+aiosqlite:///:memory:"
#
# test_engine = create_async_engine(DATABASE_URL, echo=True)
# test_async_session = async_sessionmaker(
#     test_engine,
#     expire_on_commit=False,
#     class_=AsyncSession,
# )
# Base.metadata.bind = test_engine
#
#
# async def override_get_async_session():
#     async with test_async_session() as session:
#         yield session
#
# app.dependency_overrides[get_async_session] = override_get_async_session
#
#
# @pytest.fixture(autouse=True)
# async def setup_database():
#     print('DATABASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#
# #
# # @pytest.fixture(scope='session')
# # async def ac():
# #     async with AsyncClient(app=app, base_url='http://test') as ac:
# #         yield ac
