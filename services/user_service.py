# services/user_service.py

class UserService:
    def __init__(self, user_repository, bcrypt, login_manager):
        self.user_repository = user_repository
        self.bcrypt = bcrypt
        self.login_manager = login_manager

    def register_user(self, username, email, password):
        hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email)
        self.user_repository.add(new_user)
        return new_user

    def authenticate_user(self, username, password):
        user = self.user_repository.get_by_username(username)
        if user and self.bcrypt.check_password_hash(user.password, password):
            return user
        return None