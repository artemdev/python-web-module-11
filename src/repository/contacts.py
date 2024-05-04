from typing import List
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import and_, extract
from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session, name: str = None, surname: str = None, email: str = None) -> List[Contact]:
    query = db.query(Contact)

    if name:
        query = query.filter(Contact.first_name.contains(name))
    if surname:
        query = query.filter(Contact.last_name.contains(surname))
    if email:
        query = query.filter(Contact.email.contains(email))

    return query.offset(skip).limit(limit).all()


async def get_upcoming_birthdays(db: Session) -> List[Contact]:
    today = datetime.today().date()
    in_one_week = today + timedelta(days=7)

    return db.query(Contact).filter(
        and_(
            extract('month', Contact.birthday) >= today.month,
            extract('day', Contact.birthday) >= today.day,
            extract('month', Contact.birthday) <= in_one_week.month,
            extract('day', Contact.birthday) <= in_one_week.day
        )
    ).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name,
                      last_name=body.last_name,
                      email=body.email,
                      phone=body.phone,
                      birthday=body.birthday,
                      additional_note=body.additional_note)

    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(note_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == note_id).first()
    if contact:
        contact.first_name = body.first_name,
        contact.last_name = body.last_name,
        contact.email = body.email,
        contact.phone = body.phone,
        contact.birthday = body.birthday,
        contact.additional_note = body.additional_note
        db.commit()
    return contact


async def remove_contact(note_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == note_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
