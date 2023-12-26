from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    savdo_kpi = Column(Float)
    loading_kpi = Column(Float)
    narx = Column(Integer)
    vitrina_narx = Column(Integer)
    tp_id = Column(Integer)
    image = Column(Text)
    date = Column(String)
    filial_id = Column(Integer)
    bil_value = Column(Float)
    brak_value = Column(Float)
    brak_narx = Column(Float)
    dona = Column(Float)
    status = Column(Integer)
    has_warehouse = Column(Integer)
    butun = Column(Integer)
    pressure = Column(Float)
    type = Column(String(255))
    orderNumber = Column(Integer)


