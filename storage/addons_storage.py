# addons storage file
from typing import Any
from models.addon import Addon
from storage.products_storage import BaseStrage


class AddonsStorage(BaseStrage):
    _addons: list[Addon]
    _cache: dict[str, int]

    def __init__(self):
        super().__init__("addons.json")
        self._addons = []
        self._cache = {}
        self.check_file_exist()
        self.read_from_file()
        self.refresh_cache()

    # save data to file
    def save_to_file(self):
        list_dict: list[dict[str, Any]] = []
        for item in self._addons:
            list_dict.append(item.to_dict())
        super().save_data_to_file(list_dict)

    # read data from file
    def read_from_file(self):
        dict_list = super().read_data_from_file()
        addon_list: list[Addon] = []
        for item in dict_list:
            addon_list.append(Addon.from_dict(item))
        self._addons = addon_list
    
    # refresh cache
    def refresh_cache(self):
        self._cache = {}
        for index, item in enumerate(self._addons):
            self._cache[item.item_code] = index

    # create new item and save
    def create(self, new_item: Addon):
        self._addons.append(new_item)
        self.save_to_file()
        self.refresh_cache()
    
    # read item
    def read(self, index: int) -> Addon:
        return self._addons[index]
    
    # read stroage list
    def read_list(self) -> list[Addon]:
        return self._addons.copy()
    
    # update item and save
    def update(self, index: int, new_item: Addon):
        self._addons[index] = new_item
        self.save_to_file()
        self.refresh_cache()

    # try to get cache data
    def get_cache(self, id: str) -> int | None:
        return self._cache.get(id)