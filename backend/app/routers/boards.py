from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models import Board

router = APIRouter()

@router.post("/", response_model=Board)
def create_board(board: Board, session: Session = Depends(get_session)):
    session.add(board)
    session.commit()
    session.refresh(board)
    return board

@router.get("/", response_model=list[Board])
def list_boards(session: Session = Depends(get_session)):
    return session.exec(select(Board)).all()