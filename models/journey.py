from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship


class Journey(Base):
    __tablename__ = "journey"
    id = Column(Integer, primary_key=True)
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    driver_id = Column(Integer)
    user_id = Column(Integer)
    datetime = Column(String(55))
    date = Column(String(55))
    fare = Column(Float)
    address = Column(String(255))
    top_date = Column(String(50))
    mashina_nomer = Column(String(50))
    mashina_marka = Column(String(50))
    number = Column(String(50))
    yol_kira = Column(Float)
    fare_fixed = Column(Integer)
    addition_id = Column(Integer)
    antifreeze_percent = Column(Integer)
    disabled = Column(Integer)
    filial_id = Column(Integer)

    topshiruvlar = relationship('Topshiruv', back_populates='journey')


class Topshiruv(Base):
    __tablename__ = "topshiruv"
    id = Column(Integer, primary_key=True)
    buyurtma_id = Column(Integer, ForeignKey('buyurtma.id'))
    costumer_id = (Integer, ForeignKey('costumer.id'))
    narx = Column(Float)
    tannarx = Column(Float)
    date = Column(String)
    value = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String)
    mah_id = Column(Integer)
    izoh = Column(String)
    filial_id = Column(Integer)
    seh_id = Column(Integer)
    qorovul_id = Column(Integer)
    journey_id = Column(Integer, ForeignKey('journey.id'))

    journey = relationship('Journey', back_populates='topshiruvlar')
