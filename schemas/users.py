from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from db import SessionLocal

db: Session = SessionLocal()


class UserBase(BaseModel):
    username: str
    role: str
    status: bool


class UserCreate(BaseModel):
    fullname: str
    username: str
    password_hash: str
    role: str
    status: bool = True


class UserUpdate(BaseModel):
    user_id: int
    fullname: str
    username: str
    password_hash: str
    role: str
    status: bool


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserCurrent(BaseModel):
    id: int
    username: str
    password_hash: str
    role: str
    status: bool
