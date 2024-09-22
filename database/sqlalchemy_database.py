# database/sqlalchemy_database.py

from flask_sqlalchemy import SQLAlchemy
from models.product import Product
from models.user import User
from models.order import Order

class SQLAlchemyDatabase:
    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.session = self.db.session  # Get the session for database operations

    def get_session(self):
        return self.session

    # Implement methods for products
    def get_all_products(self):
        return self.session.query(Product).all()

    def get_product_by_id(self, product_id):
        return self.session.query(Product).get(product_id)

    def update_product(self, product):
        existing_product = self.get_product_by_id(product.id)
        if existing_product:
            existing_product.name = product.name
            existing_product.price = product.price
            existing_product.stock = product.stock
            self.session.commit()
            return existing_product
        else:
            return None

    def add_product(self, product):
        self.session.add(product)
        self.session.commit()
        return product

    # Implement methods for users
    def get_user_by_id(self, user_id):
        return self.session.query(User).get(user_id)

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    # Implement methods for orders
    def add_order(self, order):
        self.session.add(order)
        self.session.commit()
        return order

    def get_orders_by_user_id(self, user_id):
        return self.session.query(Order).filter_by(user_id=user_id).all()

    # You can add more methods as required for your application