from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(255))
    username = Column(String(50), unique=True)
    password_hash = Column(String(200))
    role = Column(String(50))
    status = Column(Boolean, default=True)
    filial_id = Column(Integer)
    access_token = Column(String(400), default='')
