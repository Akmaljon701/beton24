from models.cars import Cars


def all_cars(db):
    return db.query(Cars).all()
