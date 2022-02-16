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
async def get_routines(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_client)):
    data = db.query(models.Routine).filter(current_user.id == models.Routine.client_id).all()
    print(current_user.id)
    return data


@router.get("/{name}" , response_model=List[schemas.WorkoutOut])
async def get_routine_workouts(name: str, db: Session = Depends(get_db),
                               current_user: int = Depends(oauth2.get_current_client)):
    data = db.query(models.Workout).filter(current_user.id == models.Routine.client_id,
                                           name == models.Routine.name).all()

    if not data:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"routine with name: {name} is not accessible")
    data = db.query(models.Workout).join(models.Routine).all()
    return data
