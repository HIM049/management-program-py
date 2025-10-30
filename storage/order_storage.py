
from typing import Any
from models.order import Order, OrderDetails, OrderStatus
from storage.base_storage import BaseStrage

class OrderStorage(BaseStrage):
    _orders: list[Order]
    _cache: dict[str, int]

    def __init__(self):
        super().__init__("order_storage.json")
        self._orders = []
        self._cache = {}
        self.check_file_exist()
        self.read_form_file()
        self.refresh_cache()

    def save_to_file(self):
        dict_list: list[dict[str, Any]] = []
        for item in self._orders:
            dict_list.append(item.to_dict())
        super().save_data_to_file(dict_list)
    
    def read_form_file(self):
        dict_list = super().read_data_from_file()
        order_list: list[Order] = []
        for item in dict_list:
            order_list.append(Order.from_dict(item))
        self._orders = order_list

    def refresh_cache(self):
        self._cache = {}
        for i, item in enumerate(self._orders):
            self._cache[item.id] = i

    def generate_order_code(self) -> str:
        return f"BBO-23-{len(self._orders)+1:04d}"

    def create(
            self,
            details: OrderDetails
        ):
        self._orders.append(Order(
            self.generate_order_code(),
            details,
            OrderStatus.Open
        ))
        self.save_to_file()
        self.refresh_cache()

    def read(self, index: int):
        return self._orders[index]
    
    def read_list(self) -> list[Order]:
        return self._orders.copy()
    
    def read_list_with_filter(self, status: OrderStatus) -> list[Order]:
        filtered: list[Order] = []
        for item in self._orders:
            if item.status == status:
                filtered.append(item)
        return filtered

    def update(self, index: int, new_item: Order):
        self._orders[index] = new_item
        self.save_to_file()
        self.refresh_cache()
    
    def update_by_id(self, id: str, new_item: Order):
        index = self.get_cache(id)
        if index == None:
            raise ValueError("item not found")
        self.update(index, new_item)

    def get_cache(self, code: str) -> int | None:
        return self._cache.get(code)
    
    def get_item(self, id: str) -> Order | None:
        result = self.get_cache(id)
        if result == None:
            return None
        return self.read(result)
        