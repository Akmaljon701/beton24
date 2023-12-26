from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from db import database
from functions.orders import by_costumer_id
from functions.seh import all_seh
from routes.auth import current_user
from schemas.users import UserCurrent
from utils.check_user import check_ishchi_admin

router_seh = APIRouter()


@router_seh.get('/all')
async def read_data(db: Session = Depends(database),
                    user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return all_seh(db)
