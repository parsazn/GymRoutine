from pydantic import EmailStr
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, INTEGER, VARCHAR, DateTime

from .database import Base


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    clients = relationship(
        'Client',
        secondary='routine'
    )


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    admins = relationship(
        'Admin',
        secondary='routine'
    )


class Routine(Base):
    __tablename__ = 'routine'
    admin_id = Column(Integer, ForeignKey('admin.id'), primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    name = Column(String, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    admins = relationship(Admin, backref=backref("client_assoc"))
    clients = relationship(Client, backref=backref("admins_assoc"))
    workouts = relationship("Workout", back_populates="routine_creator")


class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    set = Column(Integer, nullable=True)
    rep = Column(Integer, nullable=True)
    video_url = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    routine_creator = relationship(Routine, back_populates="workouts")
    admin_id = Column(String, ForeignKey('routine.name'))
