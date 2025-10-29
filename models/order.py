from typing import Any
from models.addon import Addon
from models.products import Product


class Delivery:
    address: str
    date: str # TODO: to date lib
    is_delivery_sameday: bool

    def __init__(self, address: str, date: str, is_delivery_sameday: bool):
        self.address = address
        self.date = date
        self.is_delivery_sameday = is_delivery_sameday

    def to_dict(self) -> dict[str, Any]:
        return {
            "address": self.address,
            "date": self.date,
            "is_delivery_sameday": self.is_delivery_sameday,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls(
            d["address"],
            d["date"],
            d["is_delivery_sameday"],
        )

class Order:
    product: Product
    addon: Addon | None

    customer_name: str
    recipient_name: str
    message: str

    delivery: Delivery | None

    def __init__(
            self, 
            product: Product, 
            addon: Addon | None, 
            customer_name: str, 
            recipient_name: str,
            message: str,
            delivery: Delivery | None
        ):
        self.product = product
        self.addon = addon
        self.customer_name = customer_name
        self.recipient_name = recipient_name
        self.message = message
        self.delivery = delivery

    def to_dict(self) -> dict[str, Any]:
        return {
            "product": self.product.to_dict(),
            "addon": self.addon.to_dict() if self.addon is not None else None,
            "customer_name": self.customer_name,
            "recipient_name": self.recipient_name,
            "message": self.message,
            "delivery": self.delivery.to_dict() if self.delivery is not None else None,
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls (
            Product.from_dict(d["product"]),
            Addon.from_dict(d["addon"]),
            d["customer_name"],
            d["recipient_name"],
            d["message"],
            Delivery.from_dict(d["delivery"]),
        )

