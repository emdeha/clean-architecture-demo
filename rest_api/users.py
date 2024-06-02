from usecase.list_users import ListUsers

from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from usecase.promote_user import PromoteUser


class UsersRestApi:
    def __init__(self, list_users: ListUsers, promote_user: PromoteUser):
        self.list_users = list_users
        self.promote_user = promote_user
        self.router = APIRouter()
        self.router.add_api_route("/", self.list, methods=["GET"])
        self.router.add_api_route("/user/{email}/promote", self.promote, methods=["PATCH"])

    def list(self) -> JSONResponse:
        return JSONResponse(content=jsonable_encoder(self.list_users.run()))

    def promote(self, email: str):
        self.promote_user.run(email)
        return Response(status_code=204)
