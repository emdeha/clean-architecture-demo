from fastapi import FastAPI

from repository.users import UsersJson
from rest_api.users import UsersRestApi
from usecase.list_users import ListUsers
from usecase.promote_user import PromoteUser

list_users = ListUsers(UsersJson("./users.json"))
promote_user = PromoteUser(UsersJson("./users.json"))
users_rest_api = UsersRestApi(list_users, promote_user)

app = FastAPI()
app.include_router(users_rest_api.router)
