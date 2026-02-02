from contextlib import asynccontextmanager
from tortoise import Tortoise
from app.core.config import settings



TORTOISE_CONFIG = {
    "connections": {"default": str(settings.DATABASE_URI)},
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.code",
                "aerich.models"
                ],
            "default_connection": "default",
        }
    },
}


@asynccontextmanager
async def lifespan(app):
    """FastAPI lifespan context for Tortoise ORM"""
    await Tortoise.init(config=TORTOISE_CONFIG)
    try:
        yield
    finally:
        await Tortoise.close_connections()
