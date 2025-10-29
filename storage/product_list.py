from typing import Any
from models.products import Product
from storage.file_storage import ProductsStorage


class ProductList(list[Product]):
    def to_dict(self) -> list[dict[str, Any]]:
        list_dict: list[dict[str, Any]] = []
        for item in self:
            list_dict.append(item.to_dict())

        return list_dict
    
    @classmethod
    def from_dict(cls, list_dict: list[dict[str, Any]]):
        products = ProductList()
        for item in list_dict:
            products.append(Product.from_dict(item))
        return cls(products)
    
    # read data from file
    def read_from_file(self):
        self = ProductsStorage().read_list_from_file()

    # save data to file
    def save_to_file(self):
        ProductsStorage().save_list_to_file(self)