from typing import List, Optional
from .order import Order

class Customer:
    def _init_(self, name: str):
        self.name = name
        self._orders: List['Order'] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name length must be between 1 and 15 characters")
        self._name = value

    def orders(self) -> List['Order']:
        return list(self._orders)

    def coffees(self) -> List['Coffee']:
        unique_coffees = {order.coffee for order in self._orders}
        return list(unique_coffees)

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        from lib.classes.order import Order
        order = Order(customer=self, coffee=coffee, price=price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee: 'Coffee') -> Optional['Customer']:
        if not coffee.orders():
            return None

        spending = {}
        for order in coffee.orders():
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price

        max_spent = max(spending.values())
        max_customers = [c for c, amt in spending.items() if amt == max_spent]

        return max_customers[0]

    def _eq_(self, other):
        if not isinstance(other, Customer):
            return False
        return self.name == other.name

    def _hash_(self):
        return hash(self.name)

    def _repr_(self):
        return f"Customer(name={self.name!r})"