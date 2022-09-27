from crypt import methods
from urllib import response
from app import app,response
from app.controller import UserController
from flask import request

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return('hello ersa app')

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user,'success')

@app.route('/file-upload', methods=['POST'])
def uploads():
    return UserController.upload()

@app.route('/user', methods=['GET', 'POST'])
@jwt_required()
def users():
    if request.method == 'GET':
        return UserController.index()
    else :
        return UserController.save()

@app.route('/userAdmin', methods=['POST'])
@jwt_required()
def useradmin():
    return UserController.buatAdmin()


@app.route('/user/<id>', methods=['PUT', 'DELETE'])
@jwt_required()
def userdel(id):
    if request.method == 'PUT':
        return UserController.updateUser(id)
    elif request.method == 'DELETE': 
        return UserController.userdelete(id)

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()