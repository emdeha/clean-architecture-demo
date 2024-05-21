from fastapi import FastAPI

from repository.users import UsersJson
from rest_api.users import UsersRestApi
from usecase.list_users import ListUsers

list_users = ListUsers(UsersJson("./users.json"))
users_rest_api = UsersRestApi(list_users)

app = FastAPI()
app.include_router(users_rest_api.router)
