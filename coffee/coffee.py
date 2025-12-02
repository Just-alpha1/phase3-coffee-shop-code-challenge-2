from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order
    from .customer import Customer


class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must have at least 3 characters")

        self._name = name
        self._orders: List['Order'] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must have at least 3 characters")
        self._name = value

    @property
    def orders(self) -> List['Order']:
        return list(self._orders)

    @property
    def customers(self) -> List['Customer']:
        # collect unique customers from orders
        unique_customers = {order.customer for order in self._orders}
        return list(unique_customers)

    def num_orders(self) -> int:
        return len(self._orders)

    def average_price(self) -> float:
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Coffee):
            return False
        return self._name == other._name

    def __hash__(self) -> int:
        return hash(self._name)

    def __repr__(self) -> str:
        return f"Coffee(name={self._name!r})"