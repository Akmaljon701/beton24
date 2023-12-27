from datetime import datetime
import pytz
from sqlalchemy import desc, func, Integer
from sqlalchemy.orm import joinedload

from models.cars import Cars
from models.journey import Journey, Topshiruv
from fastapi.exceptions import HTTPException

from models.orders import Order
from utils.pagination import is_datetime_valid


def create_journey(user, form, db):
    if not is_datetime_valid(form.datetime):
        raise HTTPException(status_code=422, detail="Vaqt noto'g'ri kiritildi!")

    car = db.query(Cars).filter_by(name=form.mashina_marka, nomer=form.mashina_nomer).first()
    if car: driver_id = car.driver_id
    else: driver_id = 0

    buyurtma = db.query(Order).filter_by(id=form.buyurtma_id).first()
    if buyurtma:
        if buyurtma.top_value < form.value:
            buyurtma.top_value -= form.value
            buyurtma.topshirildi_value += form.value
            buyurtma.narx = form.narx
            db.commit()
        else:
            raise HTTPException(status_code=400, detail="Topshirish soni buyurtma sonidan ko'p!")
    else:
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi!")

    post_journey = Journey(
        fare=0,
        addition_id=0,
        antifreeze_percent=0,
        disabled=0,
        driver_id=driver_id,
        datetime=form.datetime,
        yol_kira=form.yol_kira,
        mashina_nomer=form.mashina_nomer,
        mashina_marka=form.mashina_marka,
        number=form.number,
        user_id=user.id,
        date=form.datetime,
        address=buyurtma.address,
        filial_id=buyurtma.filial_id,
        costumer_id=buyurtma.costumer_id,
        fare_fixed=0,
    )
    db.add(post_journey)
    db.flush()

    post_topshiruv = Topshiruv(
        buyurtma_id=form.buyurtma_id,
        journey_id=post_journey.id,
        value=form.value,
        narx=form.narx,
        seh_id=form.seh_id,
        user_id=user.id,
        date=form.datetime,
        tannarx=0,
        type="top",
        mah_id=buyurtma.product_id,
        izoh="",
        filial_id=buyurtma.filial_id,
        qorovul_id=0,
    )

    db.add(post_topshiruv)
    db.flush()
    db.commit()
    raise HTTPException(status_code=201, detail="Qo'shildi!!")


def last_journey_number(db):
    last_journey = (
        db.query(Journey).filter(
            Journey.disabled == 0,
            func.length(Journey.number) > 0,
            func.cast(Journey.number, Integer) is not None
        ).order_by(func.cast(Journey.number, Integer).desc()).first()
    )

    max_number = int(last_journey.number) if last_journey else None
    return {"number": f"{max_number + 1}"}


def all_journeys(db):
    return db.query(Journey).filter(Journey.fare_fixed == 0).options(joinedload(Journey.topshiruvlar)).all()


def journey_by_id(journey_id, db):
    journey = db.query(Journey).filter_by(id=journey_id).options(joinedload(Journey.topshiruvlar)).first()
    if journey: return journey
    raise HTTPException(status_code=404, detail="Bunday id topilmadi!")


def delete_journey(journey_id, db):
    journey = db.query(Journey).filter_by(id=journey_id).options(joinedload(Journey.topshiruvlar)).first()
    if journey:
        journey.delete()
        db.commit()
        raise HTTPException(status_code=200, detail="O'chirildi!")
    raise HTTPException(status_code=404, detail="Bunday id topilmadi!")
