# repositories/order_repository.py

class OrderRepository:
    def __init__(self, database):
        self.database = database

    def add(self, order):
        return self.database.add_order(order)

    def get_by_user_id(self, user_id):
        return self.database.get_orders_by_user_id(user_id)