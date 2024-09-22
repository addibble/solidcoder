# config.py

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///store.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COMPRESS_ALGORITHM = 'gzip'
    CORS_HEADERS = 'Content-Type'
    API_ENDPOINT = os.environ.get('API_ENDPOINT', 'https://api.example.com')
    USE_API_DATABASE = os.environ.get('USE_API_DATABASE', 'False').lower() in ('true', '1', 't')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    USE_API_DATABASE = False  # Use local database in development
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    USE_API_DATABASE = True  # Use API database in production