from typing import Any
from models.products import Product
from storage.base_storage import BaseStrage

# products storage file
class ProductsStorage(BaseStrage):
    _products: list[Product]
    _cache: dict[str, Any]

    def __init__(self):
        super().__init__("products.json")
        self.check_file_exist()
        self.read_from_file()
        self.refresh_cache()

    # save data to file
    def save_to_file(self):
        dict_list: list[dict[str, Any]] = []
        for item in self._products:
            dict_list.append(item.to_dict())
        super().save_data_to_file(dict_list)

    # read data from file
    def read_from_file(self):
        dict_list = super().read_data_from_file()
        product_list: list[Product] = []
        for item in dict_list:
            product_list.append(Product.from_dict(item))
        self._products = product_list
    
    # refresh cache
    def refresh_cache(self):
        self._cache = {}
        for index, item in enumerate(self._products):
            self._cache[item.item_code] = index

    # create new item and save
    def create(self, new_item: Product):
        self._products.append(new_item)
        self.save_to_file()
        self.refresh_cache()
    
    # read item
    def read(self, index: int) -> Product:
        return self._products[index]
    
    # read storage list
    def read_list(self) -> list[Product]:
        return self._products.copy()
    
    # update item and save
    def update(self, index: int, new_item: Product):
        self._products[index] = new_item
        self.save_to_file()
        self.refresh_cache()

    # try to get cache data
    def get_cache(self, id: str) -> Any | None:
        return self._cache.get(id)