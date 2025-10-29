
from typing import Any


class Addon:
    item_code: str
    item_name: str
    price: int
    is_available: bool

    def __init__(self, item_code: str, item_name: str, price: int, is_available: bool):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
        self.is_available = is_available

    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls(
            d["item_code"], 
            d["item_name"],
            d["price"],
            d["is_available"],
        )
    
    def to_dict(self) -> dict[str, str]:
        return {
            "item_code": self.item_code,
            "item_name": self.item_name,
            "price": str(self.price),
            "is_available": str(self.is_available)
        }
    
    def to_list(self) -> list[str]:
        return [self.item_code, self.item_name, str(self.price), str(self.is_available)]
