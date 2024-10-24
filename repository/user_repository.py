from collections import defaultdict
import threading

class UserRepository:
    def __init__(self):
        self.users = defaultdict(dict)
        self.lock = threading.Lock()

    def add_or_update_user(self, user):
        with self.lock:
            self.users[user.id] = user

    def get_user(self, user_id):
        with self.lock:
            return self.users.get(user_id)  # Return the User object or None if not found

# Singleton instance of UserRepository
user_repository = UserRepository()
