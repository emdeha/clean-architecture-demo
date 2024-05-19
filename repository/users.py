import json
from typing import List

from usecase.list_users import UsersRepository, User


class UsersHardcoded(UsersRepository):
    def __init__(self, users: List[User]):
        self.users = users

    def list_users(self) -> List[User]:
        return self.users


class UsersJson(UsersRepository):
    def __init__(self, users_path: str):
        self.users_path = users_path

    def list_users(self) -> List[User]:
        with open(self.users_path) as users_json:
            return list(
                map(
                    lambda user: User(name=user["name"], email=user["email"], phone=user["phone"]),
                    json.load(users_json)
                )
            )
