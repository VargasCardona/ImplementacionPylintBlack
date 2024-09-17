"""
This module defines the Pydantic model for a cat.
"""

from pydantic import BaseModel, Field


class Cat(BaseModel):
    """Pydantic model for a cat."""

    id: int
    name: str
    color: str
    age: int = Field(..., gt=0)
    breed: str
    weight: float = Field(..., gt=0)
    owner_id: int
