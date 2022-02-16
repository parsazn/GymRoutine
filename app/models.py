from pydantic import EmailStr
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, func, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, INTEGER, VARCHAR, DateTime

from .database import Base


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
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
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    admins = relationship(
        'Admin',
        secondary='routine'
    )


class Routine(Base):
    __tablename__ = 'routine'
    admin_id = Column(Integer, ForeignKey('admin.id'), primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    name = Column(String, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    admins = relationship(Admin, backref=backref("client_assoc"))
    clients = relationship(Client, backref=backref("admins_assoc"))



class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    set = Column(Integer, nullable=True)
    rep = Column(Integer, nullable=True)
    video_url = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    routine_admin = Column(Integer)
    routine_client = Column(Integer)
    routine_name = Column(String)
    __table_args__ = (ForeignKeyConstraint([routine_admin, routine_client, routine_name],
                                           [Routine.admin_id, Routine.client_id, Routine.name]), {})
