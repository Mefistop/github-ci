# import pytest
# from httpx import AsyncClient
# from python_advanced.module_30_ci_linters.homework.tests.conftest import app
# from fastapi.testclient import TestClient
#
#
# @pytest.mark.asyncio
# async def test_hello():
#     async with AsyncClient(app=app, base_url='http://test') as ac:
#         response = await ac.get('/')
#         assert response.status_code == 200
#         assert response.json()[0] == "Hello world"
#
#
# @pytest.mark.asyncio
# async def test_add_dish():
#     print("START TESTSSSSSSSSSSSSSSSSSSSSSS")
#     request_data = {
#             "name_dish": "Test",
#             "cooking_time": 45,
#             "number_of_views": 0,
#             "list_of_ingredients": "list",
#             "description": "delicious"
#         }
#     async with AsyncClient(app=app, base_url='http://test') as ac:
#         response = await ac.post('/cookbook', json=request_data)
#         assert response.status_code == 200
#
# #
# # @pytest.mark.asyncio
# # async def test_get_dish(ac: AsyncClient):
# #     response = await ac.get('/cookbook')
# #     assert response.status_code == 200
# #     assert response.json()['name_dish'] == 'Test'
# #     assert len(response.json()) == 1
