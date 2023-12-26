from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    driver_id = Column(Integer)
    filial_id = Column(Integer)
    rent = Column(Integer)
    category = Column(String(255))
    number = Column(String(255))
