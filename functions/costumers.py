from sqlalchemy.orm import joinedload
from models.costumers import Costumer

from sqlalchemy import select, and_, join
from models.orders import Order
from models.product import Product
from models.costumers import Costumer



# def all_customers_with_orders(db):
#     customers_with_orders = db.query(Costumer).filter(Costumer.orders.any()).all()
#     return customers_with_orders
from models.shartnoma import Shartnoma


def all_customers_with_orders(user, db):
    qabul_qilingan = (
        select()
        .add_columns(Order.id, Order.order_id, Order.costumer_id)
        .select_from(
            join(Order, Costumer, onclause=Order.costumer_id == Costumer.id)
            .join(Product, onclause=Order.product_id == Product.id)
        )
        .where(
            and_(
                Order.top_value > 0,
                Costumer.filial_id == user.filial_id
            )
        )
        .group_by(Order.order_id, Costumer.id)
    )

    result = db.execute(qabul_qilingan)
    qabul_qilingan_list = result.fetchall()

    response_data = [{"id": item[0],
                      "shartnoma": db.query(Shartnoma).filter_by(id=item[1]).first(),
                      "customer": db.query(Costumer).filter_by(id=item[2]).first()} for item in qabul_qilingan_list]

    return response_data
