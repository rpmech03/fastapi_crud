from user import route as UserRoute
from configs.connection import DATABASE_URL
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.staticfiles import StaticFiles
from user import api as apiRoute
from user import api as UsersRoute

app = FastAPI()

db_url =  DATABASE_URL()

app.mount('/static', StaticFiles(directory = "static"), name= "static")
app.include_router(UserRoute.router)
# app.include_router(apiRoute.router, prefix = "api/")
app.include_router(UserRoute.router, tags=["user"])

register_tortoise(
    app,
    db_url=db_url,
    modules={'models':['user.models']},
    generate_schemas = True,
    add_exception_handlers =True
)
