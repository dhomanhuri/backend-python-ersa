from datetime import datetime, timedelta
from fileinput import filename
from app.model.user import User
from app.model.gambar import Gambar
import os
from flask import request
from app import response, app, db, uploadconfig
import uuid
from werkzeug.utils import secure_filename
from flask_jwt_extended import *


def upload():
    try:
        judul = request.form.get('judul')
        
        if 'file' not in request.files:
            return response.response.badRequest([],"file salah")

        file = request.files['file']

        if file.filename == '':
            return response.badRequest([],'file tidak ada')

        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'],renamefile))

            uploads = Gambar(judul=judul, pathname=renamefile)
            db.session.add(uploads)
            db.session.commit()

            return response.success(
                {
                    'judul' : judul,
                    'pathname' : renamefile
                },
                "sukses upload"
            )
        else:
            return response.badRequest([],"file gagal disimpan")

    except Exception as e:
        print(e)

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
        
        users = User(name=name, email=email, level=level, password=password)
        # users.setPassword(password, method='pbkdf2:sha256', salt_length=16)
        users.setPassword(password, method='sha256')
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
                'level' : level
            }
        ]

        user = User.query.filter_by(id=id).first()
        user.name = name
        user.email = email
        user.password = password
        user.level = level

        db.session.commit()

        return response.success(input, "Sukses update data user")

    except Exception as e:
        print(e)

def userdelete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "Data user kosong")

        db.session.delete(user)
        db.session.commit()

        return response.success('', 'berhasil delete user')

    except Exception as e:
        print(e)

def buatAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Admin!')
    except Exception as e:
        print(e)



def singleObjectData(data):
    data = {
        'id' : data.id,
        'name': data.name,
        'email' : data.email,
        'level' : data.level
    }

    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        # print(email)
        # print(password)
        user = User.query.filter_by(email=email).first()
        # print(user)
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Kombinasi password salah')

        
        data2 = singleObjectData(user)

        # ini_time_for_now = datetime.now()
        expires = timedelta(days=7)
        expires_refresh = timedelta(days=7)
        # print(expires)
        acces_token = create_access_token(data2, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data2, expires_delta=expires_refresh)
        print(acces_token)
        return response.success({
            "data" : data2,
            "access_token" : acces_token,
            "refresh_token" : refresh_token,
        }, "Sukses Login!")
        
    except Exception as e:
        print(e)