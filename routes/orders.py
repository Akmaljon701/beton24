from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from db import database
from functions.orders import by_costumer_id
from routes.auth import current_user
from schemas.users import UserCurrent
from utils.check_user import check_ishchi_admin

router_order = APIRouter()


@router_order.get('/by_costumer_id')
async def orders_data_by_costumer_id(costumer_id, db: Session = Depends(database),
                                     user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return by_costumer_id(costumer_id, db)
