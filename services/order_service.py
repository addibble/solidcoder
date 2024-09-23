# services/order_service.py

class OrderService:
    def __init__(self, order_repository, product_service):
        self.order_repository = order_repository
        self.product_service = product_service

    def create_order(self, user_id, product_id, quantity):
        product = self.product_service.get_product_by_id(product_id)
        if product.is_in_stock(quantity):
            product_service.update_stock(-quantity)
            order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
            self.order_repository.add(order)
            return order
        else:
            logging.warning(f"Insufficient stock for product {product_id}")
            return None

    def get_orders_by_user(self, user_id):
        return self.order_repository.get_by_user_id(user_id)

    def process_bulk_orders(self, user_id, orders):
        processed_orders = []
        total_revenue = 0

        for order_data in orders:
            product = self.product_service.get_product_by_id(order_data['product_id'])
            if not product:
                logging.warning(f"Product ID {order_data['product_id']} does not exist.")
                continue  # Skip if product does not exist
            if product.stock >= order_data['quantity']:
                # Update stock
                self.product_service.update_stock(product.id, -order_data['quantity'])
                # Calculate total
                order_total = product.price * order_data['quantity']
                total_revenue += order_total
                # Create order
                order = Order(user_id=user_id, product_id=product.id, quantity=order_data['quantity'])
                self.order_repository.add(order)
                # Append to processed orders
                processed_orders.append({
                    'product_id': product.id,
                    'quantity': order_data['quantity'],
                    'order_total': order_total
                })
            else:
                logging.warning(f"Insufficient stock for product {product.id}")
        return processed_orders, total_revenue