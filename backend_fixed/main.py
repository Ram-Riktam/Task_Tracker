import asyncio, logging
from aiohttp import web
import aiohttp_cors
from app.routes import setup_routes
from app.db.database import init_db
from app.config import FRONT_END_URL, FRONT_END_URL_2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def on_startup(app: web.Application):
    await init_db()
    logger.info("Database initialized.")

def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)

    
    cors = aiohttp_cors.setup(app, defaults={
        origin: aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        ) for origin in [FRONT_END_URL, FRONT_END_URL_2, "*"]
    })

   
    for route in list(app.router.routes()):
        cors.add(route)

    app.on_startup.append(on_startup)
    return app

if __name__ == "__main__":
    web.run_app(create_app(), host="0.0.0.0", port=8000)
