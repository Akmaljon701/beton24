from pydantic import BaseModel, validator, Field
from typing import Optional, List
from sqlalchemy.orm import Session


class JourneyCreate(BaseModel):
    datetime: str
    yol_kira: float
    mashina_nomer: str
    mashina_marka: str
    value: float
    narx: float
    number: str
    seh_id: int
    costumer_id: int
    driver_id: int
