from typing import Any
from models.addon import Addon
from storage.file_storage import AddonsStorage

class AddonList(list[Addon]):
    def to_dict(self) -> list[dict[str, Any]]:
        list_dict: list[dict[str, Any]] = []
        for item in self:
            list_dict.append(item.to_dict())
        return list_dict
    
    @classmethod
    def from_dict(cls, list_dict: list[dict[str, Any]]):
        addons = AddonList()
        for item in list_dict:
            addons.append(Addon.from_dict(item))
        return cls(addons)
    
    # read data from file
    def read_from_file(self):
        self = AddonsStorage().read_list_from_file()
    
    # save data to file
    def save_to_file(self):
        AddonsStorage().save_list_to_file(self)