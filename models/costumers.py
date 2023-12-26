from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship


class Costumer(Base):
    __tablename__ = "costumer"
    id = Column(Integer, primary_key=True)
    top_sana = Column(String(50))
    filial_id = Column(Integer)
    name = Column(String(100))
    company_name = Column(String(255))
    date = Column(String(50))
    phone = Column(String(9))
    status = Column(String(11))
    address = Column(Text)
    address_orienter = Column(Text)
    balance = Column(Float)
    balance2 = Column(Float)
    cashback_balance = Column(Float)
    nas_date = Column(String(50))
    user_id = Column(Integer)
    costumer_turi = Column(String(255))
    anonim = Column(Integer)
    inn = Column(Integer)
    bank_number = Column(Integer)

    orders = relationship('Order', back_populates='costumer')
