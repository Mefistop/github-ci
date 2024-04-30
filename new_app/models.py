from sqlalchemy import Column, Integer, String

from .database import Base


class CookBook(Base):
    __tablename__ = "cookbook"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name_dish = Column(String, index=True)
    number_of_views = Column(Integer, index=True, default=0)
    cooking_time = Column(Integer, index=True)
    list_of_ingredients = Column(String, index=True)
    description = Column(String, index=True)
