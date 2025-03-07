from repository.user_repository import UserRepository
from models.user import User
from database.db import db

class UserRepositoryImpl(UserRepository):
    def get_all(self):
        users = User.query.all()
        return users
    
    def create(self, user_entity: User):
        user = User(name=user_entity.name, email=user_entity.email)
        db.session.add(user)
        db.session.commit()