from enum import Enum
from typing import Any
from models.addon import Addon
from models.products import Product
from services.table import Table, TableLayout, TableRow

class OrderStatus(Enum):
    Open = 1
    Cancelled = 2
    Preparing = 3
    Ready = 4
    Closed = 5

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
    
class OrderDetails:
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
            delivery: Delivery | None,
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
        addon: Addon | None = None
        delivery: Addon | None = None
        if d["addon"] != None:
            addon = Addon.from_dict(d["addon"])
        if d["delivery"] != None:
            Delivery.from_dict(d["delivery"])
            
        return cls(
            Product.from_dict(d["product"]),
            addon,
            d["customer_name"],
            d["recipient_name"],
            d["message"],
            delivery,
        )

    def get_price(self) -> int:
        total: int = 0
        total += self.product.price
        if self.addon != None:
            total += self.addon.price

        if self.delivery != None:
            # delivery fee
            total += 35
            if self.delivery.is_delivery_sameday:
                total += 35
        return total
    
    def get_summary_table(self) -> Table:
        table = Table()
        layout_products = TableLayout(4)

        layout_products.append_row(TableRow(["Item:", self.product.item_name, self.product.item_code, f"${self.product.price}"]))
        # have addon
        if self.addon != None:
            layout_products.append_row(TableRow(["Addon:", self.addon.item_name, self.addon.item_code, f"${self.addon.price}"]))
        else:
            layout_products.append_row(TableRow(["Addon:", "None", "", "$0"]))

        layout_products.append_blank_row()

        # have delivery
        if self.delivery != None:
            layout_products.append_row(TableRow(["Delivery date:", self.delivery.date, "", ""]))
            
            # need same day delivery
            price: int = 35 if self.delivery.is_delivery_sameday else 0
            status: str = "Yes" if self.delivery.is_delivery_sameday else "No"
            layout_products.append_row(TableRow(["Same day delivery:", status, "", f"${price}"]))

            layout_products.append_row(TableRow(["Delivery charges:", "", "", "$35"]))
        else:
            layout_products.append_row(TableRow(["Collect by:", "Store pickup", "", ""]))
        layout_products.append_row(TableRow(["Total:", "", "", f"${self.get_price()}"]))

        # blank line
        layout_products.append_blank_row()
        table.append_layout(layout_products)

        layout_details = TableLayout(2)
        layout_details.append_row(TableRow(["Customer’s name:", self.customer_name]))
        layout_details.append_row(TableRow(["Recipient’s name:", self.recipient_name]))
        layout_details.append_row(TableRow(["Message for recipient:", self.message]))
        if self.delivery != None:
            layout_details.append_row(TableRow(["Delivery address:", self.delivery.address]))

        table.append_layout(layout_details)
        return table

class Order:
    id: str
    order_datails: OrderDetails
    status: OrderStatus

    def __init__(
            self, 
            id: str,
            order_datails: OrderDetails,
            status: OrderStatus
        ):
        self.id = id
        self.order_datails = order_datails
        self.status = status

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "order_details": self.order_datails.to_dict(),
            "status": self.status.value
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]):
        return cls (
            d["id"],
            OrderDetails.from_dict(d["order_details"]),
            OrderStatus(d["status"])
        )
    
    def to_list(self) -> list[str]:
        return [self.id, self.order_datails.product.item_name ,self.status.name]

