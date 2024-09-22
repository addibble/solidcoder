
# repositories/user_repository.py
class UserRepository:
    def __init__(self, database):
        self.database = database

    def get_by_id(self, user_id):
        return self.database.get_user_by_id(user_id)

    def add(self, user):
        return self.database.add_user(user)
