from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from db import Base, engine, database
from functions.costumers import all_customers_with_orders
from models.costumers import Costumer
from routes.auth import current_user
from schemas.users import UserCurrent
from utils.check_user import check_ishchi_admin

router_costumer = APIRouter()


@router_costumer.get('/all_have_orders')
async def costumers_data(db: Session = Depends(database),
                         user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return all_customers_with_orders(db)

