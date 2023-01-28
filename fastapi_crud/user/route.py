from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from http.client import HTTPException, HTTPResponse
from fastapi import APIRouter, Request, Form, status, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi_login.exceptions import InvalidCredentialsException
# from passlib.context import CryptContext

templates = Jinja2Templates(directory = "user/templates")

router = APIRouter()

@router.get("/registration/", response_class = HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("registration.html", {"request":request,
    })