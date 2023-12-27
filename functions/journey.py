from datetime import datetime
import pytz
from sqlalchemy import desc
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
    if not car:
        raise HTTPException(status_code=404, detail="Bunday mashina mavjud emas!")
    post_journey = Journey(
        # qaysini qo'shish kerak
        fare=0.1,
        address="Null",
        addition_id=1,
        antifreeze_percent=1,
        disabled=0,
        filial_id=1,

        # podozreniya
        fare_fixed=0,
        costumer_id=form.costumer_id,

        driver_id=car.driver_id,
        datetime=form.datetime,
        yol_kira=form.yol_kira,
        mashina_nomer=form.mashina_nomer,
        mashina_marka=form.mashina_marka,
        number=form.number,
        user_id=user.id,
        status="True",
        date=form.datetime,
    )
    db.add(post_journey)
    db.flush()

    post_topshiruv = Topshiruv(
        # qaysini qo'shish kerak
        tannarx=1,
        type="",
        mah_id=1,
        izoh="",
        filial_id=1,
        qorovul_id=1,

        buyurtma_id=form.buyurtma_id,
        journey_id=post_journey.id,
        value=form.value,
        narx=form.narx,
        seh_id=form.seh_id,
        user_id=user.id,
        date=form.datetime,
    )

    buyurtma = db.query(Order).filter_by(id=form.buyurtma_id).first()
    if buyurtma:
        if buyurtma.top_value < form.value:
            buyurtma.top_value -= form.value
            buyurtma.topshirildi_value += form.value
            db.commit()
        else: raise HTTPException(status_code=400, detail="Topshirish soni buyurtma sonidan ko'p!")
    else:
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi!")

    db.add(post_topshiruv)
    db.flush()
    db.commit()
    raise HTTPException(status_code=201, detail="Qo'shildi!!")


def last_journey_number(db):
    last_journey = db.query(Journey).order_by(desc(Journey.id)).first().number
    return {"number": last_journey}


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
