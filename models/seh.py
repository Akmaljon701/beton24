from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship


class Seh(Base):
    __tablename__ = "seh"
    id = Column(Integer, primary_key=True)
    name = Column(String(111))
    shift = Column(String(255))
    hasPlan = Column(Float)
    filial_id = Column(Integer)
    emergency = Column(Integer)
    salaryDay = Column(Integer)
    