from fastapi import APIRouter, Depends, Query
from pydantic import Field
from sqlalchemy.orm import Session, joinedload
from db import Base, engine, database
from functions.journey import create_journey, last_journey_number, all_journeys, journey_by_id, delete_journey
from routes.auth import current_active_user, current_user
from schemas.journey import JourneyCreate
from schemas.users import UserCurrent
from utils.check_user import check_ishchi_admin

router_journey = APIRouter()


@router_journey.post('/create')
async def create_journey_data(form: JourneyCreate, db: Session = Depends(database),
                              user: UserCurrent = Depends(current_user)):
    return create_journey(user, form, db)


@router_journey.get('/last_journey_number')
async def read_data(db: Session = Depends(database)):
    return last_journey_number(db)


@router_journey.get('/all')
async def read_data(db: Session = Depends(database),
                    user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return all_journeys(db)


@router_journey.get('/by_id')
async def read_data(journey_id: int = Query(..., ge=0), db: Session = Depends(database),
                    user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return journey_by_id(journey_id, db)


@router_journey.delete('/delete')
async def delete_data(journey_id: int = Query(..., ge=0), db: Session = Depends(database),
                      user: UserCurrent = Depends(current_user)):
    check_ishchi_admin(user)
    return delete_journey(journey_id, db)


