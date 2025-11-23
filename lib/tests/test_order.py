import pytest
from lib.classes.order import Order
from lib.classes.customer import Customer
from lib.classes.coffee import Coffee

def test_order_initialization_and_properties():
    cust = Customer("Alvin")
    coffee = Coffee("Cappuccino")

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(cust, "not a coffee", 5.0)
