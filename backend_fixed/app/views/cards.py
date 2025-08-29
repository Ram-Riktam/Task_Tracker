from aiohttp import web
from sqlalchemy import select
from datetime import datetime, timezone
from app.db.database import AsyncSessionLocal
from app.models.card_models import Card

utcnow = lambda: datetime.now(timezone.utc)

async def list_cards(request):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Card).order_by(Card.created_at.desc()))
        return web.json_response([c.as_dict() for c in result.scalars().all()])

async def create_card(request):
    data = await request.json()
    title = (data.get("title") or "").strip()
    if not title:
        return web.json_response({"error": "title is required"}, status=400)

    async with AsyncSessionLocal() as session:
        last = (await session.execute(select(Card).order_by(Card.created_at.desc()))).scalars().first()
        if last and last.task_number.startswith("TASK-"):
            try: num = int(last.task_number.split("-")[1])
            except: num = 0
            task_number = f"TASK-{num + 1:03d}"
        else:
            task_number = "TASK-001"

        card = Card(
            task_number=task_number, title=title,
            description=data.get("description"),
            status=data.get("status", "todo"),
            added_by=data.get("added_by", "frontend"),
        )
        session.add(card); await session.commit()
        return web.json_response(card.as_dict(), status=201)

async def update_card(request):
    data, card_id = await request.json(), request.match_info["id"]
    async with AsyncSessionLocal() as session:
        card = (await session.execute(select(Card).where(Card.id == card_id))).scalars().first()
        if not card: return web.json_response({"error": "Card not found"}, status=404)

        for field in ["title", "description", "status", "added_by"]:
            if field in data and data[field]: setattr(card, field, data[field])
        card.updated_at = utcnow()

        await session.commit(); await session.refresh(card)
        return web.json_response(card.as_dict())

async def delete_card(request):
    card_id = request.match_info["id"]
    async with AsyncSessionLocal() as session:
        card = (await session.execute(select(Card).where(Card.id == card_id))).scalars().first()
        if not card: return web.json_response({"error": "Card not found"}, status=404)
        await session.delete(card); await session.commit()
        return web.json_response({"message": "Card deleted"})
