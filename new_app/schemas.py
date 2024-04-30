from pydantic import BaseModel


class BaseCookBook(BaseModel):
    name_dish: str
    cooking_time: int


class CookBookIn(BaseCookBook):
    number_of_views: int
    list_of_ingredients: str
    description: str

    class Config:
        orm_mode = True


class CookBookOut(CookBookIn):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class CookBookBrieflyOut(BaseCookBook):
    number_of_views: int

    class Config:
        orm_mode = True
        from_attributes = True
