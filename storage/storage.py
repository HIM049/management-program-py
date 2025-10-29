from storage.addon_list import AddonList
from storage.file_storage import AddonsStorage, ProductsStorage
from storage.product_list import ProductList

class Storage:
    products: ProductList
    addons: AddonList
    products_id_cache: dict[str, int]
    addons_id_cache: dict[str, int]

    def __init__(self):
        self.products: ProductList = ProductList()
        self.addons: AddonList = AddonList()
        self.products_id_cache = {}
        self.addons_id_cache = {}

    # init data in storage
    def init(self):
        ProductsStorage().check_file_exist()
        AddonsStorage().check_file_exist()

        self.products.read_from_file()
        self.addons.read_from_file()

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