import jwt
from flask import request, current_app

from models.user import User

def token_required(func):
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return {
                'error': 'Token not provided.',
                'detail': 'No token was provided.'
            }, 401
        
        try:
            data = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
            current_user = User.query.filter_by(id = data['id']).first()
        except:
            return {
                'error': 'Invalid token.',
                'detail': 'Provided token is invalid.'
            }, 401
        
        return func(current_user, *args, **kwargs)
  
    return decorated