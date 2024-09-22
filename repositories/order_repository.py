# repositories/order_repository.py

class OrderRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, order):
        self.db_session.add(order)
        self.db_session.commit()

    def get_by_user_id(self, user_id):
        return Order.query.filter_by(user_id=user_id).all()