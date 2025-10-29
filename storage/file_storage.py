
import json
import os
from typing import Any

from storage.addon_list import AddonList
from storage.product_list import ProductList


STORAGE_BASE_FOLDER = "./storage_file"

class BaseStrage:
    _file_path: str

    def __init__(self, file_name: str):
        self._file_path = os.path.abspath(os.path.join(STORAGE_BASE_FOLDER, file_name))

    # save to file
    def save_to_file(self, data: list[dict[str, Any]]):
        with open(self._file_path, "w") as file:
            json.dump(data, file, indent=4)
    
    # read from file
    def read_from_file(self) -> list[dict[str, Any]]:
        with open(self._file_path, "r") as file:
            return json.load(file)

    # check whether the file exist
    def check_file_exist(self):
        if not os.path.exists(self._file_path):
            os.makedirs(os.path.abspath(STORAGE_BASE_FOLDER), exist_ok=True)
            init_data = []
            try:
                with open(self._file_path, "w") as file:
                    json.dump(init_data, file, indent=4)
            except:
                print("failed to create file")

# products storage file
class ProductsStorage(BaseStrage):
    def __init__(self):
        super().__init__("products.json")

    def save_list_to_file(self, data: ProductList):
        super().save_to_file(data.to_dict())

    def read_list_from_file(self) -> ProductList:
        dict_list = super().read_from_file()
        return ProductList.from_dict(dict_list)

# addons storage file
class AddonsStorage(BaseStrage):
    def __init__(self):
        super().__init__("addons.json")

    def save_list_to_file(self, data: AddonList):
        super().save_to_file(data.to_dict())

    def read_list_from_file(self) -> AddonList:
        dict_list = super().read_from_file()
        return AddonList.from_dict(dict_list)