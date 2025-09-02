from aiohttp import web
from app.views.cards import list_cards, create_card, update_card, delete_card

def setup_routes(app: web.Application):
    app.router.add_get("/cards", list_cards)
    app.router.add_post("/cards", create_card)
    app.router.add_put("/cards/{id}", update_card)
    app.router.add_delete("/cards/{id}", delete_card)
