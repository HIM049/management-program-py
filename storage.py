
import json
from products import Categories, Product

storage_path = "./storage/products.json"

class Storage:
    products: list[dict[str, any]]

    def __init__(self):
        self.products: list[Product] = []

    def append(self, product: dict[str, any]):
        self.products.append(product)

    def save_to_file(self):
        # TODO: catch errors on opening file
        with open(storage_path, "w") as file:
            json.dump(self.products, file, indent=4)

    def read_from_file(self):
        with open(storage_path, "r") as file:
            data = json.load(file)
            
        for product in data:
            self.products.append(Product.from_dict(product))

# Global object
STORAGE = Storage()
