from usecase.list_users import ListUsers, User

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class UsersRestApi:
    def __init__(self, list_users: ListUsers):
        self.list_users = list_users
        self.router = APIRouter()
        self.router.add_api_route("/", self.list, methods=["GET"])

    def list(self) -> JSONResponse:
        return JSONResponse(content=jsonable_encoder(self.list_users.run()))
