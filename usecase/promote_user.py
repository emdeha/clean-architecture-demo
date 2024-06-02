from usecase.repository import UsersRepository
from usecase.user import Promotion


class PromoteUser:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def run(self, email: str):
        user = self.repository.find_user_by_email(email)
        if user.promotion is None:
            user.promotion = Promotion.DEVELOPER
        elif user.promotion == Promotion.DEVELOPER:
            user.promotion = Promotion.MANAGER
        self.repository.update_user(user)
