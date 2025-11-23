from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from lib.classes.order import Order
    from lib.classes.customer import Customer

class Coffee:
    def __init__(self, name: str):
        self.name = name
        self._orders: List['Order'] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string"),
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    def orders(self) -> List['Order']:
        return list(self._orders)

    def customers(self) -> List['Customer']:
        unique_customers = {order.customer for order in self._orders}
        return list(unique_customers)

    def num_orders(self) -> int:
        return len(self._orders)

    def average_price(self) -> float:
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __eq__(self, other):
        if not isinstance(other, Coffee):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Coffee(name={self.name!r})"
