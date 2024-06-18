from fastapi import FastAPI
from that_depends.providers import DIContextMiddleware

import exceptions
from api import endpoints

from exceptions import DatabaseValidationError
from settings import settings


def get_app() -> FastAPI:
    _app = FastAPI(
        title=settings.service_name,
        debug=settings.debug,
    )

    _app.include_router(endpoints.ROUTER, prefix="/api")


    _app.add_middleware(DIContextMiddleware)

    _app.add_exception_handler(
        DatabaseValidationError,
        exceptions.database_validation_exception_handler,  # type: ignore[arg-type]
    )

    return _app


application = get_app()
