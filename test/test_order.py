import pytest
from coffee.order import Order
from coffee.customer import Customer
from coffee.coffee import Coffee

def test_order_initialization_and_properties():
    cust = Customer("Alvin")
    coffee = Coffee("Cappuccino")

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(cust, "not a coffee", 5.0)
    with pytest.raises(TypeError):
        Order(cust, coffee, "not a price")
    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(cust, coffee, 15.0)

    order = Order(cust, coffee, 5.5)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.5