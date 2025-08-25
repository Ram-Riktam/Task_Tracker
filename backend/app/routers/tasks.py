from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import Task

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/", response_model=list[Task])
def list_tasks(session: Session = Depends(get_session)):
    return session.exec(select(Task)).all()