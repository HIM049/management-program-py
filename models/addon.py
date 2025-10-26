
class Addon:
    item_code: str
    item_name: str
    price: int
    available: bool

    def __init__(self, item_code: str, item_name: str, price: int, available: bool):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
        self.available = available

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            d["item_code"], 
            d["item_name"],
            d["price"],
            d["available"],
        )
    
    def to_dict(self) -> dict[str, str]:
        return {
            "item_code": self.item_code,
            "item_name": self.item_name,
            "price": self.price,
            "available": self.available
        }
    
    def to_list(self) -> list[str]:
        return [self.item_code, self.item_name, self.price, self.available]
