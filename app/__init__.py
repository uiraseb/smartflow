# app/__init__.py
from flask import Flask
from flask_restx import Api
from .extensions import db, make_celery

api = Api(title="SmartFlow API", version="1.0", description="Automação com IA")

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartflow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'jwt-super-secret'

    db.init_app(app)
    api.init_app(app)

    @app.route('/health')
    def health():
        return {"status": "healthy"}, 200

    with app.app_context():
        db.create_all()

    return app, None  # celery = None por enquanto

app, celery = create_app()