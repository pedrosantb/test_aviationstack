"""
App main file. 
This is the execution point of the project.

"""

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from routers.pages import pages_router

app = FastAPI(
    title="Teste Aviation Stack"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pages_router)

# test debugging
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

