from repository.user_repository import user_repository
from models.user_model import User

def add_user_service(user):
    for _ in range(10):  # Limit the number of attempts to prevent infinite loops
        current_user = User(first_name=user["first_name"], last_name=user["last_name"])

        if not user_repository.get_user(current_user.id):  # Check if the user ID is unique
            user_repository.add_or_update_user(current_user)  # Add the user
            return current_user
    raise Exception("Unable to add user due to UUID collision.")

def get_user_service(user_id):
    user = user_repository.get_user(user_id)
    if user is None:
        raise ValueError("User not found.")  # Raise an exception if user is not found
    return user