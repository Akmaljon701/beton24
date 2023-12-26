from models.seh import Seh


def all_seh(db):
    return db.query(Seh).all()
