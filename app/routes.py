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

@app.route('/userAdmin', methods=['POST'])
def useradmin():
    return UserController.buatAdmin()


@app.route('/user/<id>', methods=['PUT', 'DELETE'])
def userdel(id):
    if request.method == 'PUT':
        return UserController.updateUser(id)
    elif request.method == 'DELETE': 
        return UserController.userdelete(id)

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()