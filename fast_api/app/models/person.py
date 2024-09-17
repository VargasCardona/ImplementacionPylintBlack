"""
This module defines the Pydantic model for a person.
"""

from pydantic import BaseModel, Field, EmailStr


class Person(BaseModel):
    """Pydantic model for a person."""

    id: int
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr
    address: str
    is_employed: bool
    salary: float
