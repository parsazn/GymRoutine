from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

from pydantic.types import conint

from app.models import Workout


class ClientOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    lastname: str
    created_at: datetime

    class Config:
        orm_mode = True


class AdminOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


class AdminCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class RoutineBase(BaseModel):
    name: str
    created_at: datetime
    admin_id: int
    client_id: int


class WorkoutBase(BaseModel):
    name: str


class Workout(WorkoutBase):
    id: int
    set = int
    rep = int
    video_url = str
    image_url = str

    class Config:
        orm_mode = True


class WorkoutOut(BaseModel):
    id: int
    name: str
    set = int
    rep = int
    video_url = str
    image_url = str
    routine_id = int

    class Config:
        orm_mode = True


class RoutineCreate(RoutineBase):
    pass


class Routine(RoutineBase):
    workouts: WorkoutOut

    class Config:
        orm_mode = True


class RoutineCreate(RoutineBase):
    pass


class RoutineOut(BaseModel):
    name: str
    created_at: datetime
    admin_id: int
    client_id: int

    class Config:
        orm_mode = True


class WorkoutCreate(WorkoutBase):
    pass


class ClientCreate(BaseModel):
    email: EmailStr
    name: str
    lastname: str
    password: str


class ClientLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
