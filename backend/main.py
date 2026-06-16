from fastapi import FastAPI

from app.database import Base, engine
from app.routes.subjects import router as subjects_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(subjects_router)


@app.get("/")
def root():
    return {"message": "Study Assistant API"}