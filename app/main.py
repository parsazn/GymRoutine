from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from app import models, schemas
from app.database import engine
from .routers import user, auth, admin, routine
from .database import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(routine.router)
##
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    data = db.query(models.Routine).join(models.Workout).first()

    return data


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
