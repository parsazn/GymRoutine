from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
