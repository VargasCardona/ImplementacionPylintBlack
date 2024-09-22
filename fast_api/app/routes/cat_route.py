"""
This module defines the routes for cat-related operations in the FastAPI application.
Routes:
    - POST /cats/: Create a new cat.
    - GET /cats: Retrieve a list of all cats.
    - GET /cats/{cat_id}: Retrieve a specific cat by their ID.
    - PUT /cats/{cat_id}: Update a specific cat by their ID.
    - DELETE /cats/{cat_id}: Delete a specific cat by their ID.
Functions:
    - create_cats(cat: Cat): Creates a new cat with the provided details.
    - get_cats(): Retrieves a list of all cats from the database.
    - get_cat(cat_id: int): Retrieves a specific cat by their ID. 
      Returns an error message if the cat is not found.
    - update_cat(cat_id: int, cat: Cat): Updates a specific cat by their ID.
    - delete_cat(cat_id: int): Deletes a specific cat by their ID.
Dependencies:
    - CatModel: The database model for cats.
    - Cat: The Pydantic model for cat data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

from fastapi import APIRouter, Body

# pylint: disable=import-error
from database import CatModel
from models.cat import Cat

# pylint: enable=import-error

cat_route = APIRouter()


@cat_route.post("/cats/")
def create_cats(cat: Cat = Body(...)):
    """
    Create a new cat.

    Args:
        cat (Cat): The cat object containing the catname, color, and age.

    Returns:
        None
    """
    CatModel.create(
        name=cat.name,
        color=cat.color,
        age=cat.age,
        breed=cat.breed,
        weight=cat.weight,
        owner_id=cat.owner_id,
    )
    return {"message": "Cat created successfully"}


@cat_route.get("/cats")
def get_cats():
    """
    Retrieve a list of cats from the database.

    This function queries the CatModel to select all cats with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a cat.
    """
    cat = CatModel.select().where(CatModel.id > 0).dicts()
    return list(cat)


@cat_route.get("/cats/{cat_id}")
def get_cat(cat_id: int):
    """
    Retrieve a cat by their ID.

    Args:
        cat_id (int): The ID of the cat to retrieve.

    Returns:
        CatModel: The cat object if found.
        dict: An error message if the cat is not found.
    """
    print(cat_id)
    try:
        cat = CatModel.get(CatModel.id == cat_id)
        return cat
    except CatModel.DoesNotExist:
        return {"error": "Cat not found"}


@cat_route.put("/cats/{cat_id}")
def update_cat(cat_id: int, cat: Cat = Body(...)):
    """
    Update a cat by their ID.

    Args:
        cat_id (int): The ID of the cat to update.
        cat (Cat): The updated cat object containing the catname, color, and age.

    Returns:
        None
    """
    CatModel.update(
        name=cat.name,
        color=cat.color,
        age=cat.age,
        breed=cat.breed,
        weight=cat.weight,
        owner_id=cat.owner_id,
    ).where(CatModel.id == cat_id).execute()
    return {"message": "Cat updated successfully"}


@cat_route.delete("/cats/{cat_id}")
def delete_cat(cat_id: int):
    """
    Delete a cat by their ID.

    Args:
        cat_id (int): The ID of the cat to delete.

    Returns:
        None
    """
    CatModel.delete().where(CatModel.id == cat_id).execute()
    return {"message": "Cat deleted successfully"}
