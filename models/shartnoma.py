from datetime import datetime
import pytz
from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship


class Shartnoma(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    total_price = Column(Float)
    total_debit = Column(Float)
    total_credit = Column(Float)
    created_at = Column(String, default=datetime.now(pytz.timezone('Asia/Tashkent')))
    status = Column(String(255))
    tasdiqladi = Column(Integer)
    number = Column(Integer)
    user_id = Column(Integer)
    filial_id = Column(Integer)
    documentUrl	= Column(String(255))

