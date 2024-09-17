"""
This module initializes the FastAPI application and sets up the database connection
"""

from fastapi import FastAPI

from starlette.responses import RedirectResponse

from routes.person_route import person_route
from routes.cat_route import cat_route

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
app.include_router(person_route, prefix="/api/persons", tags=["Persons"])

# -------- Cat --------
app.include_router(cat_route, prefix="/api/cats", tags=["Cats"])
