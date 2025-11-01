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
    rating: tuple[float, int] | None

    def __init__(self, item_code: str, item_name: str, category: Categories, price: int, rating: tuple[float, int] | None, is_available: bool = True):
        self.item_code = item_code
        self.item_name = item_name
        self.category = category
        self.price = price
        self.is_available = is_available
        self.rating = rating

    # transfer to dict
    def to_dict(self) -> dict[str, Any]:
        return {
            "item_code": self.item_code,
            "item_name": self.item_name,
            "category": self.category.value,
            "price": self.price,
            "is_available": self.is_available,
            "rating": self.rating,
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls(
            d["item_code"],
            d["item_name"],
            Categories(d["category"]),
            d["price"],
            d["rating"],
            d["is_available"]
        )

    def to_list(self) -> list[str]:
        return [
            self.item_code, 
            self.item_name, 
            self.category.name, 
            str(self.price), 
            str(self.is_available), 
            f"{self.rating[0]} ({self.rating[1]} rating)" if self.rating != None else "No rating"
        ]

    def add_rating(self, rating: float):
        # limit range
        if rating > 5 : rating = 5
        if rating < 0 : rating = 0

        # first rating
        if self.rating == None:
            self.rating = (rating, 1)
            return
        new_rating = (self.rating[0] * self.rating[1] + rating) / (self.rating[1] + 1)
        self.rating = (new_rating, self.rating[1]+1)