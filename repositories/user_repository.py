# repositories/user_repository.py

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, user):
        self.db_session.add(user)
        self.db_session.commit()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()