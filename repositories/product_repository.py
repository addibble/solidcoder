# repositories/product_repository.py

class ProductRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all(self):
        return Product.query.all()

    def get_by_id(self, product_id):
        return Product.query.get(product_id)

    def update(self, product):
        self.db_session.commit()