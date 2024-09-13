from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key

from starlette.responses import RedirectResponse

from routes.user_route import user_router

app = FastAPI(
    title="Microservicio de usuarios",
    version="2.0",
    contact={
        "name": "Nicolas Duran Garces",
        "url": "https://github.com/NicolasDuranGarces",
        "email": "nicolas.duran@eam.edu.co",
    },
)


@app.get("/", include_in_schema=False)
def read_root():
    return


app.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_api_key)],
)
