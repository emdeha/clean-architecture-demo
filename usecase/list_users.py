from abc import ABC, abstractmethod
from typing import List


class User:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def __eq__(self, other):
        return self.name == other.name and \
            self.email == other.email and \
            self.phone == other.phone


class UsersRepository(ABC):
    @abstractmethod
    def list_users(self) -> List[User]:
        pass


class ListUsers:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def run(self) -> List[User]:
        return self.repository.list_users()
