from storage.addons_storage import AddonsStorage
from storage.order_storage import OrderStorage
from storage.products_storage import ProductsStorage


class Storage:
    products: ProductsStorage
    addons: AddonsStorage
    orders: OrderStorage

    def __init__(self):
        self.products = ProductsStorage()
        self.addons = AddonsStorage()
        self.orders = OrderStorage()

# Global object
STORAGE = Storage()