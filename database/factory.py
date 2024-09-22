# database/factory.py

from .sqlalchemy_database import SQLAlchemyDatabase
from .api_database import APIDatabase

class DatabaseFactory:
    @staticmethod
    def create_database(config):
        if config['USE_API_DATABASE']:
            return APIDatabase(config['API_ENDPOINT'])
        else:
            return SQLAlchemyDatabase(config['SQLALCHEMY_DATABASE_URI'])