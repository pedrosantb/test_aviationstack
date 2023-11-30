from fastapi.responses import RedirectResponse, HTMLResponse

from fastapi import APIRouter, Request, status, HTTPException, Response

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
pages_router = APIRouter()

@pages_router.get("/")
async def index(request: Request):
    '''
    Index page
    '''
    return templates.TemplateResponse("index.html", {"request": request})
    