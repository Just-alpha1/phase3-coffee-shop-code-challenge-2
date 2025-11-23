from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from .customer import Customer
   from .coffee import Coffee

class Order:
    def _init_(self, customer: 'Customer', coffee: 'Coffee', price: float):
        if not hasattr(customer, 'name'):
            raise TypeError("customer must be a Customer instance")
        if not hasattr(coffee, 'name'):
            raise TypeError("coffee must be a Coffee instance")
        self._customer = customer
        self._coffee = coffee
        self.price = price

    @property
    def customer(self) -> 'Customer':
        return self._customer

    @property
    def coffee(self) -> 'Coffee':
        return self._coffee