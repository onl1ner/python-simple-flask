import time

from flask import request, Blueprint, jsonify

from models.article import Article

from utils.database import db
from utils.token_required import token_required

article = Blueprint('article', __name__)

@article.route('/', methods = ['GET'])
def get_articles():
    def json(articles):
        return jsonify(list(map(lambda a: a.serialize(), articles)))
    
    author_id = request.args.get('author-id')

    if author_id:
        return json(Article.query.filter_by(author_id = author_id).all())
        
    return json(Article.query.all())

@article.route('/create', methods = ['POST'])
@token_required
def create_article(user):
    author_id = user.id
    created_at = time.time()
    text = request.get_json()['text']

    if not text:
        return {
            'error': 'Text not provided.',
            'detail': 'No text was provided to create article.'
        }, 400
    
    article = Article(
        author_id = author_id,
        created_at = created_at,
        text = text
    )

    db.session.add(article)
    db.session.commit()

    return article.serialize()