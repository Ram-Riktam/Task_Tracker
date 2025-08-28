from aiohttp import web
from sqlalchemy import select
from datetime import datetime, timezone
from app.database import AsyncSessionLocal
from app.models import Card

def utcnow():
    return datetime.now(timezone.utc)


async def list_cards(request):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Card).order_by(Card.created_at.desc()))
        cards = result.scalars().all()
        return web.json_response([c.as_dict() for c in cards])


async def create_card(request):
    data = await request.json()
    title = (data.get("title") or "").strip()
    if not title:
        return web.json_response({"error": "title is required"}, status=400)

    async with AsyncSessionLocal() as session:
        
        result = await session.execute(select(Card).order_by(Card.created_at.desc()))
        last_card = result.scalars().first()
        if last_card and last_card.task_number.startswith("TASK-"):
            try:
                last_num = int(last_card.task_number.split("-")[1])
            except Exception:
                last_num = 0
            new_task_number = f"TASK-{last_num + 1:03d}"
        else:
            new_task_number = "TASK-001"

        card = Card(
            task_number=new_task_number,
            title=title,
            description=data.get("description"),
            status=data.get("status", "todo"),
            added_by=data.get("added_by", "frontend"),
        )
        session.add(card)
        await session.commit()
        await session.refresh(card)
        return web.json_response(card.as_dict(), status=201)


async def update_card(request):
    card_id = request.match_info["id"] 

    data = await request.json()
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Card).where(Card.id == card_id))
        card = result.scalars().first()
        if not card:
            return web.json_response({"error": "Card not found"}, status=404)

        if "title" in data and data["title"] is not None:
            card.title = data["title"]
        if "description" in data:
            card.description = data["description"]
        if "status" in data and data["status"]:
            card.status = data["status"]
        if "added_by" in data and data["added_by"]:
            card.added_by = data["added_by"]

        card.updated_at = utcnow()

        await session.commit()
        await session.refresh(card)
        return web.json_response(card.as_dict())


async def delete_card(request):
    card_id = request.match_info["id"]  
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Card).where(Card.id == card_id))
        card = result.scalars().first()
        if not card:
            return web.json_response({"error": "Card not found"}, status=404)

        await session.delete(card)
        await session.commit()
        return web.json_response({"message": "Card deleted"})