from utils.database import db

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    created_at = db.Column(db.BigInteger)
    
    text = db.Column(db.String())

    def serialize(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'created_at': self.created_at,
            'text': self.text
        }

    pass