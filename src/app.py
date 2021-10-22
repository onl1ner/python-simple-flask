import os
import dotenv
import jwt

from flask import Flask, request

from utils.database import db

dotenv.load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

from modules.auth import auth
from modules.article import article

app.register_blueprint(auth, url_prefix = '/auth')
app.register_blueprint(article, url_prefix = '/articles')

@app.route('/protected')
def protected():
    token = request.args.get('token')

    if not token:
        return "<h1>Hello, no token was provided</h1>"
    
    try:
        jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=['HS256'])
    except:
        return "<h1>Hello, Could not verify the token</h1>"
    
    return "<h1>Hello, token which is provided is correct </h1>"

if __name__ == "__main__":
    app.run(debug = True)