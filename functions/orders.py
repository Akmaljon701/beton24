from sqlalchemy.orm import joinedload

from models.costumers import Costumer
from models.orders import Order
from utils.pagination import one_obj
from fastapi.exceptions import HTTPException


def by_costumer_id(costumer_id, db):
    if one_obj(Costumer, costumer_id, db).first():
        return db.query(Order).filter(Order.costumer_id == costumer_id,
                                      Order.top_value > 0,
                                      Order.topshirildi_value > 0).options(joinedload(Order.product)).all()
    raise HTTPException(status_code=404, detail="Costmer topilmadi!")
