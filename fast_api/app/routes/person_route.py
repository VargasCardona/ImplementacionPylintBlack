"""
This module defines the routes for user-related operations in the FastAPI application.
Routes:
    - POST /users/: Create a new user.
    - GET /users: Retrieve a list of all users.
    - GET /users/{user_id}: Retrieve a specific user by their ID.
Functions:
    - create_users(user: User): Creates a new user with the provided details.
    - get_users(): Retrieves a list of all users from the database.
    - get_user(user_id: int): Retrieves a specific user by their ID. 
      Returns an error message if the user is not found.
Dependencies:
    - UserModel: The database model for users.
    - User: The Pydantic model for user data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

from fastapi import APIRouter, Body

from models.user import UserModel as User

user_route = APIRouter()


@user_route.post("/users/")
def create_users(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object containing the username, password, and email.

    Returns:
        None
    """
    # UserModel.create(username=user.username, password=user.password, email=user.email)
    print(user)
    return {"message": "User created successfully"}


@user_route.get("/users")
def get_users():
    """
    Retrieve a list of users from the database.

    This function queries the UserModel to select all users with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a user.
    """
    # user = UserModel.select().where(UserModel.id > 0).dicts()
    # return list(user)
    return {"message": "Get all users"}


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserModel: The user object if found.
        dict: An error message if the user is not found.
    """
    print(user_id)
    try:
        # user = UserModel.get(UserModel.id == user_id)
        # return user
        return {"message": "Get user by ID"}
    # except UserModel.DoesNotExist:
    except FileNotFoundError as e:
        # return {"error": "User not found"}
        print(e)
        return {"message": "User not found"}
