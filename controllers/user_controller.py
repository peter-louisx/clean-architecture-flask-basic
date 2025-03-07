# MVC Architecture
# from flask import request, jsonify 
# from models.user import User 
# from database.db import db 
 
# def get_users(): 
#     users = User.query.all() 
#     return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users]) 
 
# def create_user(): 
#     data = request.get_json() 
#     new_user = User(name=data['name'], email=data['email']) 
#     db.session.add(new_user) 
#     db.session.commit() 
#     return jsonify({"message": "User created successfully"}), 201

# Clean Architecture
from flask import request, jsonify
from use_case.user_usecase import UserUsecase
from repository.user_repository_impl import UserRepositoryImpl
from domain.user import UserEntity

user_repository = UserRepositoryImpl()
user_usecase = UserUsecase(user_repository)

def get_users():
    users = user_usecase.get_all_users()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

def create_user():
    data = request.get_json()
    new_user = UserEntity(None, data['name'], data['email'])
    user_usecase.create_user(new_user)
    return jsonify({"message": "User created successfully"}), 201