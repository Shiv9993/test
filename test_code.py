import re
from typing import Dict

class UserAlreadyExistsError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class UserService:
    def __init__(self):
        self.users: Dict[str, str] = {}  # email -> name

    def is_valid_email(self, email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def register_user(self, name: str, email: str) -> str:
        if not self.is_valid_email(email):
            raise InvalidEmailError(f"Invalid email: {email}")
        if email in self.users:
            raise UserAlreadyExistsError(f"User already registered: {email}")
        self.users[email] = name
        return f"User {name} registered successfully."

    def get_user(self, email: str) -> str:
        return self.users.get(email, None)
