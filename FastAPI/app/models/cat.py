"""
This module defines the Pydantic model for a cat.
"""

from pydantic import BaseModel, Field


class Cat(BaseModel):
    """Pydantic model for a cat."""

    name: str
    color: str
    age: int = Field(..., gt=0)
    breed: str
    weight: float
    is_indoor: bool
