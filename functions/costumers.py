from sqlalchemy.orm import joinedload

from models.costumers import Costumer


def all_customers_with_orders(db):
    customers_with_orders = db.query(Costumer).filter(Costumer.orders.any()).all()
    return customers_with_orders
