
import json
import os
from models.addon import Addon
from products import Categories, Product

storage_path = "./storage"
products_storage_path = os.path.join(storage_path, "products.json")
addons_storage_path = os.path.join(storage_path, "addons.json")

class Storage:
    products: list[Product]
    addons: list[Addon]
    products_id_cache: dict[str, int]
    addons_id_cache: dict[str, int]

    def __init__(self):
        self.products: list[Product] = []
        self.addons: list[Addon] = []
        self.products_id_cache = {}
        self.addons_id_cache = {}

    # append a new item to storage
    def append_product(self, product: Product):
        self.products.append(product)
        self.save_to_file()
        self.refresh_cache()

    # update item and save to file
    def update_product(self, index: int, new_product: Product):
        self.products[index] = new_product
        self.save_to_file()
        self.refresh_cache()

    # append a new item to storage
    def append_addon(self, addon: Addon):
        self.addons.append(addon)
        self.save_to_file()
        self.refresh_cache()

    # update item and save to file
    def update_addon(self, index: int, new_addon: Addon):
        self.addons[index] = new_addon
        self.save_to_file()
        self.refresh_cache()

    # save storage to file
    def save_to_file(self):
        # TODO: catch errors on opening file
        save_products_to_file(self.products)
        save_addons_to_file(self.addons)

    # load storage from file
    def read_from_file(self):
        self.products = read_products()
        self.addons = read_addons()

    # cache to search item by id
    def refresh_cache(self):
        self.products_id_cache = {}
        for i, product in enumerate(self.products):
            self.products_id_cache[product.item_code] = i

        self.addons_id_cache = {}
        for i, addon in enumerate(self.addons):
            self.addons_id_cache[addon.item_code] = i

# Global object
STORAGE = Storage()

def read_products() -> list[Product]:
    with open(products_storage_path, "r") as file:
        data = json.load(file)
        
    products: list[Product] = []
    for product in data:
        products.append(Product.from_dict(product))

    return products

def read_addons() -> list[Addon]:
    with open(addons_storage_path, "r") as file:
        data = json.load(file)
        
    addons: list[Addon] = []
    for addon in data:
        print(type(Addon.from_dict(addon)))
        addons.append(Addon.from_dict(addon))

    return addons

def save_products_to_file(products: list[Product]) :
    with open(products_storage_path, "w") as file:
        dict_list: list[dict] = []
        for product in products:
            dict_list.append(product.to_dict())

        json.dump(dict_list, file, indent=4)

def save_addons_to_file(addons: list[Addon]):
    with open(addons_storage_path, "w") as file:
        dict_list: list[dict] = []
        for addon in addons:
            dict_list.append(addon.to_dict())

        json.dump(dict_list, file, indent=4)

def check_storage_file(path):
    if not os.path.exists(path):
        os.makedirs(storage_path, exist_ok=True)
        
        initial_data = []
        try:
            with open(path, 'w') as file:
                json.dump(initial_data, file, indent=4)

        except:
            pass