from app import app
from app.controller import UserController
from flask import request

@app.route('/')
def index():
    return('hello ersa app')

@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else :
        return UserController.save()

@app.route('/user/<id>', methods=['PUT', 'DELETE'])
def userdel(id):
    if request.method == 'PUT':
        return UserController.updateUser(id)
    else : 
        return UserController.userdelete(id)