from http.client import HTTPException, HTTPResponse
from fastapi import APIRouter, Request,Form,status,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
# from fastapi_login.exceptions import InvalidCredentialsException
# from fastapi_login import LoginManager
from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from tortoise.functions import Sum
from slugify import slugify
from datetime import datetime
from passlib.context import CryptContext
import secrets
from .models import *

templates = Jinja2Templates(directory = "user/templates")

router = APIRouter()
SECRET = 'your-secret-key'
router = APIRouter()
# manager = LoginManager(SECRET, token_url='/auth/token')
templates = Jinja2Templates(directory="user/templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/registration/", response_class = HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("registration.html", {"request":request,
    })

@router.post('/add_registration/',)
async def create_user(request: Request,email: str = Form(...),
                      name: str = Form(...), \
                      phone: str = Form(...),
                      password: str = Form(...)):
    if "_messages" in request.session:
        print(request.session["_messages"][0]['username']) 
        phone = request.session["_messages"][0]['username']
        
    elif "_messages" in request.session:
        print(request.session["_messages"][0]['username']) 
        email = request.session["_messages"][0]['username']
        
    else:
        user_obj = await User.create(email=email,name=name,
                                     phone=phone
                                     ,password= get_password_hash(password))
       
    return RedirectResponse("/login/", status_code=status.HTTP_302_FOUND)