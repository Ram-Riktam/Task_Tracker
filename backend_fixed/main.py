import asyncio
import logging
from aiohttp import web
import aiohttp_cors

from app.routes import setup_routes
from app.database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def on_startup(app: web.Application):
    await init_db()
    logger.info("Database initialized.")

def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)

   
    cors = aiohttp_cors.setup(app, defaults={
        "http://localhost:5173": aiohttp_cors.ResourceOptions(
            allow_credentials=True, expose_headers="*", allow_headers="*"
        ),
        "http://127.0.0.1:5173": aiohttp_cors.ResourceOptions(
            allow_credentials=True, expose_headers="*", allow_headers="*"
        ),
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True, expose_headers="*", allow_headers="*"
        ),
    })
    for route in list(app.router.routes()):
        cors.add(route)

    app.on_startup.append(on_startup)
    return app

if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=8000)