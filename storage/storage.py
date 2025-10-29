from storage.addons_storage import AddonsStorage
from storage.products_storage import ProductsStorage


class Storage:
    products: ProductsStorage
    addons: AddonsStorage

    def __init__(self):
        self.products = ProductsStorage()
        self.addons = AddonsStorage()

# Global object
STORAGE = Storage()