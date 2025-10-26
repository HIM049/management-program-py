
import json
from products import Categories, Product

storage_path = "./storage/products.json"

class Storage:
    products: list[Product]
    id_cache: dict[str, any]

    def __init__(self):
        self.products: list[Product] = []
        self.id_cache = {}

    # append a new item to storage
    def append(self, product: Product):
        self.products.append(product)
        self.save_to_file()
        self.refresh_cache()

    # update item and save to file
    def update(self, index: int, new_product: Product):
        self.products[index] = new_product
        self.save_to_file()
        self.refresh_cache()

    # save storage to file
    def save_to_file(self):
        # TODO: catch errors on opening file
        with open(storage_path, "w") as file:
            dict_list: list[dict] = []
            for product in self.products:
                dict_list.append(product.to_dict())

            json.dump(dict_list, file, indent=4)

    # load storage from file
    def read_from_file(self):
        with open(storage_path, "r") as file:
            data = json.load(file)
            
        for product in data:
            self.products.append(Product.from_dict(product))

    # cache to search item by id
    def refresh_cache(self):
        self.id_cache = {}
        for i, product in enumerate(self.products):
            self.id_cache[product.item_code] = i

# Global object
STORAGE = Storage()
