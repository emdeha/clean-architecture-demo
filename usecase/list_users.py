from typing import List

from usecase.repository import UsersRepository
from usecase.user import User


class ListUsers:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def run(self) -> List[User]:
        return self.repository.list_users()
