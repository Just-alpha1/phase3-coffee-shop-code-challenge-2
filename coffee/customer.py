from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 chars")
        self._name = value

   
    def orders(self):
        from .order import Order
        return [order for order in Order.all if order.customer == self]


    def coffees(self):
        return list({order.coffee for order in self.orders()})

    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Customer who spent the most on a given coffee"""
        from .order import Order
        spenders = {}
        for order in Order.all:
            if order.coffee == coffee:
                spenders[order.customer] = spenders.get(order.customer, 0) + order.price

        if not spenders:
            return None

        return max(spenders, key=spenders.get)
