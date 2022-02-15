from typing import List

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/routines",
    tags=['Routine']
)


@router.get("/", response_model=List[schemas.RoutineOut])
async def root(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_client)):
    data = db.query(models.Routine).filter(current_user.id == models.Routine.client_id).all()
    print(current_user.id)
    return data

