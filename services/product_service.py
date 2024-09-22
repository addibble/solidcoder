# services/product_service.py

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_all_products(self):
        return self.product_repository.get_all()

    def get_product_by_id(self, product_id):
        return self.product_repository.get_by_id(product_id)

    def generate_inventory_report(self):
        products = self.get_all_products()
        total_value = self.calculate_total_value(products)
        low_stock_items = self.find_low_stock_items(products)
        report = self.format_product_data(products)
        return {
            'total_products': len(products),
            'total_value': total_value,
            'low_stock_items': low_stock_items,
            'products': report
        }

    def calculate_total_value(self, products):
        return sum(product.price * product.stock for product in products)

    def find_low_stock_items(self, products, threshold=10):
        return [product.name for product in products if product.stock < threshold]

    def format_product_data(self, products):
        return [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'stock': product.stock
            }
            for product in products
        ]

    def update_stock(self, product_id, quantity_change):
        product = self.get_product_by_id(product_id)
        if product:
            product.stock += quantity_change
            self.product_repository.update(product)

    def update_product(self, product):
        return self.product_repository.update(product)
