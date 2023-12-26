from fastapi import APIRouter, Depends, Query
from pydantic import Field
from sqlalchemy.orm import Session, joinedload
from db import Base, engine, database
from functions.cars import all_cars
from functions.journey import create_journey, last_journey_number, all_journeys, journey_by_id
from routes.auth import current_active_user, current_user
from schemas.journey import JourneyCreate
from schemas.users import UserCurrent
from utils.check_user import check_ishchi_admin

router_cars = APIRouter()


@router_cars.get('/all')
async def read_data(db: Session = Depends(database),
                    user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return all_cars(db)

