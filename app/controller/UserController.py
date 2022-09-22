from app.model.user import User
# from app.model.gambar import Gambar
from flask import request
# import os
from app import response, app, db #, uploadconfig
# import uuid
# from werkzeug.utils import secure_filename


def index():
    try:
        user = User.query.all()
        data = formatarray(user)
        return response.success(data, "success")

    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        'email' : data.email,
        'password' : data.password,
        'level' : data.level,
        'created_at' : data.created_at,
        'updated_at' : data.updated_at
    }
    return data

def save():
    try:
        name = request.form.get('name'),
        email = request.form.get('email'),
        password = request.form.get('password'),
        level = 1
        
        users = User(name=name, email=email, password=password, level=level)
        db.session.add(users)
        db.session.commit()

        return response.success("", "berhasil menambah data user")

    except Exception as e:
        print(e)

def updateUser(id):
    try:
        name = request.form.get('name'),
        email = request.form.get('email'),
        password = request.form.get('password'),
        level = 1
        
        input = [
            {
                'name' : name,
                'email' : email,
                'password' : password,
                'level' : 1
            }
        ]

        user = User.query.filter_by(id=id).first()
        user.name = name
        user.email = email
        user.password = password
        user.level = 1

        db.session.commit()

        return response.success(input, "Sukses update data user")

    except Exception as e:
        print(e)

def userdelete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], "Data dosen kosong")

        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'berhasil delete user')

    except Exception as e:
        print(e)