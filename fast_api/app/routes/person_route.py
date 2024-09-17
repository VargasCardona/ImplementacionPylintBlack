"""
This module defines the routes for person-related operations in the FastAPI application.
Routes:
    - POST /persons/: Create a new person.
    - GET /persons: Retrieve a list of all persons.
    - GET /persons/{person_id}: Retrieve a specific person by their ID.
    - PUT /persons/{person_id}: Update a specific person by their ID.
    - DELETE /persons/{person_id}: Delete a specific person by their ID.
Functions:
    - create_persons(person: Person): Creates a new person with the provided details.
    - get_persons(): Retrieves a list of all persons from the database.
    - get_person(person_id: int): Retrieves a specific person by their ID. 
      Returns an error message if the person is not found.
    - update_person(person_id: int, person: Person): Updates a specific person by their ID.
    - delete_person(person_id: int): Deletes a specific person by their ID.
Dependencies:
    - PersonModel: The database model for persons.
    - Person: The Pydantic model for person data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

from fastapi import APIRouter, Body

from database import PersonModel
from models.person import Person

person_route = APIRouter()

@person_route.post("/persons/")
def create_persons(person: Person = Body(...)):
    """
    Create a new person.

    Args:
        person (Person): The person object containing the name, age, email,
        address, is_employed and salary.

    Returns:
        None
    """
    PersonModel.create(
        name=person.name,
        age=person.age,
        email=person.email,
        address=person.address,
        is_employed=person.is_employed,
        salary=person.salary,
    )
    return {"message": "Person created successfully"}


@person_route.get("/persons")
def get_persons():
    """
    Retrieve a list of persons from the database.

    This function queries the PersonModel to select all persons with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a person.
    """
    person = PersonModel.select().where(PersonModel.id > 0).dicts()
    return list(person)


@person_route.get("/persons/{person_id}")
def get_person(person_id: int):
    """
    Retrieve a person by their ID.

    Args:
        person_id (int): The ID of the person to retrieve.

    Returns:
        PersonModel: The person object if found.
        dict: An error message if the person is not found.
    """
    try:
        person = PersonModel.get(PersonModel.id == person_id)
        return person
    except PersonModel.DoesNotExist:
        return {"error": "Person not found"}


@person_route.put("/persons/{person_id}")
def update_person(person_id: int, person: Person = Body(...)):
    """
    Update a person by their ID.

    Args:
        person_id (int): The ID of the person to update.
        person (Person): The person object containing the updated details.

    Returns:
        None
    """
    PersonModel.update(
        name=person.name,
        age=person.age,
        email=person.email,
        address=person.address,
        is_employed=person.is_employed,
        salary=person.salary,
    ).where(PersonModel.id == person_id).execute()
    return {"message": "Person updated successfully"}


@person_route.delete("/persons/{person_id}")
def delete_person(person_id: int):
    """
    Delete a person by their ID.

    Args:
        person_id (int): The ID of the person to delete.

    Returns:
        None
    """
    PersonModel.delete().where(PersonModel.id == person_id).execute()
    return {"message": "Person deleted successfully"}
