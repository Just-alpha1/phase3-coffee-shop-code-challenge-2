from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from lib.classes.order import Order
    from lib.classes.customer import Customer

class Coffee:
    def _init_(self, name: str):
        self.name = name
        self._orders: List['Order'] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    def orders(self) -> List['Order']:
        return list(self._orders)

    def _repr_(self):
        return f"Coffee(name={self.name!r})"