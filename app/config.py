# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///smartflow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-super-secret'
    SECRET_KEY = 'super-secret'
    
    # Usa Redis como broker E como result backend
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'