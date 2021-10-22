import jwt

from hashlib import sha256
from flask import request, Blueprint, current_app
from datetime import datetime, timedelta

from models.user import User
from utils.database import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods = ['POST'])
def register():
    json = request.get_json()
    
    login = json['login']

    first_name = json['first_name']
    last_name  = json['last_name']

    password = json['password']
    
    user = User.query.filter_by(login = login).first()

    if user:
        return { 
            'error': 'Record already exist.',
            'detail': 'User with the provided login already exist.'
        }, 409

    user = User(
        login = login,
        first_name = first_name,
        last_name = last_name,
        password = sha256(password.encode()).hexdigest()
    )

    db.session.add(user)
    db.session.commit()

    return user.serialize()

@auth.route('/login', methods = ['POST'])
def login():
    json = request.get_json()

    login    = json['login']
    password = json['password']

    user = User.query.filter_by(login = login).first()

    if not user:
        return {
            'error': 'Record not exist.',
            'detail': 'User with the provided login does not exist.'
        }, 404
    
    pass_hash = sha256(password.encode()).hexdigest()

    if user.password == pass_hash:
        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes = 30)
        }

        token = jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm="HS256")

        return { 'access': token }, 200

    return { 
        'error': 'Wrong credentials',
        'detail': 'Entered password is incorrect.'
    }, 401