import granian
from granian.constants import Interfaces, Loops

from settings import settings


if __name__ == "__main__":
    granian.Granian(
        target="application:application",
        address="https://taxi_bot_db.up.railway.app",  # noqa: S104
        port=settings.app_port,
        interface=Interfaces.ASGI,
        log_dictconfig={"root": {"level": "INFO"}} if not settings.debug else {},
        log_level=settings.log_level,
        loop=Loops.asyncio,
    ).serve()
