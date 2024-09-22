# repositories/product_repository.py

class ProductRepository:
    def __init__(self, database):
        self.database = database

    def get_all(self):
        return self.database.get_all_products()

    def get_by_id(self, product_id):
        return self.database.get_product_by_id(product_id)

    def update(self, product):
        return self.database.update(product)
