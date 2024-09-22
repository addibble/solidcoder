# database/api_database.py

class APIDatabase:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint

    def get_all_products(self):
        response = requests.get(f"{self.api_endpoint}/products")
        return response.json()

    def get_product_by_id(self, product_id):
        response = requests.get(f"{self.api_endpoint}/products/{product_id}")
        return response.json()

    def update(self, product):
        product_data = {
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
        }
        response = requests.put(f"{self.api_endpoint}/product/{product.id}", json=product_data)
