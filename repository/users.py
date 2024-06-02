import json
from typing import List, Optional

from usecase.list_users import UsersRepository
from usecase.user import User


class UsersHardcoded(UsersRepository):
    def __init__(self, users: List[User]):
        self.users = users

    def list_users(self) -> List[User]:
        return self.users

    def find_user_by_email(self, email) -> Optional[User]:
        return next((user for user in self.users if user.email == email), None)

    def update_user(self, user_to_update: User):
        self.users[:] = [user_to_update if user.email == user_to_update.email else user for user in self.users]


class UsersJson(UsersRepository):
    def __init__(self, users_path: str):
        self.users_path = users_path

    def list_users(self) -> List[User]:
        with open(self.users_path) as users_json:
            return list(
                map(
                    lambda user: User(
                        name=user["name"],
                        email=user["email"],
                        phone=user["phone"],
                        promotion=user.get("promotion")
                    ),
                    json.load(users_json)
                )
            )

    def find_user_by_email(self, email) -> Optional[User]:
        users = self.list_users()
        return next((user for user in users if user.email == email), None)

    def update_user(self, user_to_update: User):
        users = [user_to_update if user.email == user_to_update.email else user for user in self.list_users()]
        with open(self.users_path, "w") as users_json:
            json.dump(list(map(lambda user: user.__dict__, users)), indent=2, fp=users_json)
