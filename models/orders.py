from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, and_
from sqlalchemy.orm import relationship, backref

from models.product import Product


class Order(Base):
    __tablename__ = "buyurtma"
    id = Column(Integer, primary_key=True)
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    b_user_id = Column(Integer)
    top_user_id = Column(Integer)
    transport_user_id = Column(Integer)
    product_id = Column(Integer)
    type_product_id = Column(Integer)
    value = Column(Float)
    top_value = Column(Float)
    ombor_value = Column(Float)
    transport_value = Column(Float)
    topshirildi_value = Column(Float)
    date = Column(String(50))
    top_sana = Column(String(50))
    narx = Column(Integer)
    sort = Column(Integer)
    filial_id = Column(Integer)
    yetkazish = Column(Integer)
    tannarx = Column(Float)
    order_id = Column(Integer)
    address = Column(String(255))
    yol_kira = Column(Float)
    yol_kira_value = Column(Float)

    costumer = relationship('Costumer', back_populates='orders')
    product = relationship('Product', foreign_keys=[product_id],
                           primaryjoin=lambda: and_(Product.id == Order.product_id),
                           backref=backref("product_orders"))
