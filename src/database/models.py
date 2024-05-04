from sqlalchemy import Column, Integer, String, Boolean, func, Table, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=False)
    additional_note = Column(String(150), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
