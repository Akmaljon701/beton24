from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn

# database url

DB_USERNAME = 'akmaljon'
DB_PASSWORD = 'OTPbzAbjgY8xsdd6'
DB_HOST = 'db.temir-beton.uz'
DB_PORT = 3306
DB_NAME = 'qoqon_beton'

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost:3306/template'

# import os
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# SQLALCHEMY_DATABASE_URL = 'sqlite:///'+os.path.join(BASE_DIR,'bazza.db?check_same_thread=False')

# generate SECRET_KEY
# import secrets
# secret_key = secrets.token_urlsafe(32)
# print(secret_key)


SECRET_KEY = 'SOME-SECRET-KEY'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
