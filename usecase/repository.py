from abc import ABC, abstractmethod
from typing import List, Optional

from usecase.user import User


class UsersRepository(ABC):
    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def find_user_by_email(self, email) -> Optional[User]:
        pass

    @abstractmethod
    def list_users(self) -> List[User]:
        pass
