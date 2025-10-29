from enum import Enum
from typing import Any


class Categories(Enum):
    Romantic = 1
    Birthday = 2
    GrandOpening = 3
    Condolence = 4
    Anniversary = 5


class Product:
    item_code: str
    item_name: str
    category: Categories
    price: int
    is_available: bool

    def __init__(self, item_code: str, item_name: str, category: Categories, price: int, is_available: bool = True):
        self.item_code = item_code
        self.item_name = item_name
        self.category = category
        self.price = price
        self.is_available = is_available

    # transfer to dict
    def to_dict(self) -> dict[str, Any]:
        return {
            "item_code": self.item_code,
            "item_name": self.item_name,
            "category": self.category.value,
            "price": self.price,
            "is_available": self.is_available,
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls(
            d["item_code"],
            d["item_name"],
            Categories(d["category"]),
            d["price"],
            d["is_available"],
        )

    def to_list(self) -> list[str]:
        return [self.item_code, self.item_name, self.category.name, str(self.price), str(self.is_available)]
