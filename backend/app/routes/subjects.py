from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post("/")
def create_subject(subject: SubjectCreate):

    db: Session = SessionLocal()

    new_subject = Subject(
        name=subject.name
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    db.close()

    return new_subject


@router.get("/")
def get_subjects():

    db: Session = SessionLocal()

    subjects = db.query(Subject).all()

    db.close()

    return subjects