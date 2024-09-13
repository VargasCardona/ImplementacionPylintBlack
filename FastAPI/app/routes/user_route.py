from fastapi import APIRouter


user_router = APIRouter()


@user_router.get("/")
async def read_root():
    return {"Hello": "World"}
