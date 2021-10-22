from utils.database import db

class User(db.Model):
    __tablename__ = 'users'
    
    id    = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String())
    
    first_name = db.Column(db.String())
    last_name  = db.Column(db.String())

    password = db.Column(db.String())

    articles = db.relationship('Article')

    def serialize(self):
        return {
            'id': self.id,
            'login': self.login,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    pass