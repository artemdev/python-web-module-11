from datetime import datetime, date
from pydantic import BaseModel


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date
    additional_note: str


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date
    additional_note: str
    created_at: datetime

    class Config:
        from_attributes = True
