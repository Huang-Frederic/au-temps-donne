class UserEmailNotFoundException(Exception):
    def __init__(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"User with email '{self.email}' not found."
    

class UserIdNotFoundException(Exception):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __str__(self) -> str:
        return f"User with id '{self.user_id}' not found."


class UserAlreadyExistsException(Exception):
    def __init__(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"User with email '{self.email}' already exists."
    

class UserAccessDbException(Exception):
    def __init__(self, user_id: int, method: str) -> None:
        self.user_id = user_id
        self.method = method

    def __str__(self) -> str:
        if self.user_id:
            return f"Error {self.method} user '{self.user_id}'."
        else: 
            return f"Error {self.method} users."

    