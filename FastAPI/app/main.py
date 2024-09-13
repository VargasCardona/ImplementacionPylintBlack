from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key

from starlette.responses import RedirectResponse

from .models.person import Person
from .models.cat import Cat

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
    return


@app.post("/post_person")
def post_person(person: Person):
    """
    Create a new person.
    """
    print(person)


@app.post("/post_cat")
def post_cat(cat: Cat):
    """
    Create a new cat.
    """
    print(cat)
