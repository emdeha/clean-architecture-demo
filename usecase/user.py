from enum import Enum
from typing import Optional


class Promotion(str, Enum):
    DEVELOPER = "DEVELOPER"
    MANAGER = "MANAGER"


class User:
    def __init__(self, name: str, email: str, phone: str, promotion: Optional[Promotion] = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.promotion = promotion

    def __eq__(self, other):
        return self.name == other.name and \
            self.email == other.email and \
            self.phone == other.phone and \
            self.promotion == other.promotion
