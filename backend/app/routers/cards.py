from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from app.models import Card
from app.schemas import CardCreate, CardUpdate
from app.database import get_session
from datetime import datetime
from uuid import UUID

router = APIRouter(tags=["Cards"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_card(card: CardCreate, session: Session = Depends(get_session)):
    db_card = Card(
        Title=card.Title,
        Description=card.Description,
        added_by=card.added_by,
        comments=card.comments,
        status=card.status,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(db_card)
    session.commit()
    session.refresh(db_card)

    return {
        "Status": 201,
        "message": "Card created successfully...!",
        "id": db_card.id
    }

@router.get("/")
def list_cards(session: Session = Depends(get_session)):
    cards = session.query(Card).all()
    result = [
        {
            "id": card.id,
            "Title": card.Title,
            "Description": card.Description,
            "added_by": card.added_by,
            "comments": card.comments,
            "status": card.status,
            "created_at": card.created_at,
            "updated_at": card.updated_at,
        }
        for card in cards
    ]
    return {
        "status_code": 200,
        "data": result
    }

@router.put("/{card_id}")
def update_card(card_id: str, card: CardUpdate, session: Session = Depends(get_session)):
    db_card = session.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")

    # update only provided fields
    if card.Title is not None:
        db_card.Title = card.Title
    if card.Description is not None:
        db_card.Description = card.Description
    if card.added_by is not None:
        db_card.added_by = card.added_by
    if card.comments is not None:
        db_card.comments = card.comments
    if card.status is not None:
        db_card.status = card.status

    db_card.updated_at = datetime.utcnow()
    session.commit()
    session.refresh(db_card)

    # fetch updated list
    cards = session.query(Card).all()
    result = [
        {
            "id": card.id,
            "Title": card.Title,
            "Description": card.Description,
            "added_by": card.added_by,
            "comments": card.comments,
            "status": card.status,
            "created_at": card.created_at,
            "updated_at": card.updated_at,
        }
        for card in cards
    ]

    return {
        "status": 200,
        "message": "Card updated successfully",
        "data": result
    }


# -------------------------
# DELETE - Delete Card
# -------------------------
@router.delete("/{card_id}")
def delete_card(card_id: str, session: Session = Depends(get_session)):
    db_card = session.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")

    session.delete(db_card)
    session.commit()

    # fetch updated list
    cards = session.query(Card).all()
    result = [
        {
            "id": card.id,
            "Title": card.Title,
            "Description": card.Description,
            "added_by": card.added_by,
            "comments": card.comments,
            "status": card.status,
            "created_at": card.created_at,
            "updated_at": card.updated_at,
        }
        for card in cards
    ]

    return {
        "status": 200,
        "message": "Card deleted successfully",
        "data": result
    }