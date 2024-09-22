"""
This module initializes the FastAPI application and sets up the database connection
"""

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

# pylint: disable=import-error
from helpers.api_key_auth import get_api_key
from routes.person_route import person_route
from routes.cat_route import cat_route

# pylint: enable=import-error

app = FastAPI(
    title="Microservice of persons and little cats",
    version="2.0",
    contact={
        "name": "Nicolás Vargas Cardona - Mateo Loaiza García",
        "url": "https://github.com/VargasCardona",
    },
)


@app.get("/", include_in_schema=False)
def read_root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """
    return RedirectResponse(url="/docs")


# -------- Person --------
app.include_router(
    person_route,
    prefix="/api/persons",
    tags=["Persons"],
    dependencies=[Depends(get_api_key)],
)

# -------- Cat --------
app.include_router(
    cat_route,
    prefix="/api/cats",
    tags=["Cats"],
    dependencies=[Depends(get_api_key)],
)
