"""
This module initializes the FastAPI application and sets up the database connection
"""

# pylint: disable=import-error
import os

from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
# pylint: enable=import-error

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    """
    Obtain the API key stored in the .env file

    Returns:
        api_key_header: The stored api key.
    """

    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "status": False,
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": "Unauthorized",
        },
    )
