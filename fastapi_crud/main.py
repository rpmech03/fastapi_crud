from user import route as UserRoute
from configs.connection import DATABASE_URL
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware
# from user import api as UserRoute

db_url =  DATABASE_URL()
middleware = [
    Middleware(SessionMiddleware, secret_key = 'super-secret')
    ]
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

app.mount('/static', StaticFiles(directory = "static"), name= "static")
app.include_router(UserRoute.router)
app.include_router(UserRoute.router, tags=["user"])

register_tortoise(
    app,
    db_url=db_url,
    modules={'models':['user.models']},
    generate_schemas = True,
    add_exception_handlers =True
)
