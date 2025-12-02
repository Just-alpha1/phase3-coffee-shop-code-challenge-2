import pytest
from coffee.customer import Customer
from coffee.coffee import Coffee
from coffee.order import Order

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a"*16)

    c = Customer("Alvin")
    assert c.name == "Alvin"
    c.name = "Sean"
    assert c.name == "Sean"
    with pytest.raises(ValueError):
        c.name = ""

def test_create_order_and_orders_coffees():
    cust = Customer("Alvin")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Red eye")

    order1 = cust.create_order(coffee1, 5.0)
    order2 = cust.create_order(coffee2, 7.5)

    orders = cust.orders()
    coffees = cust.coffees()

    assert order1 in orders
    assert order2 in orders
    assert coffee1 in coffees
    assert coffee2 in coffees
    assert len(coffees) == 2

def test_most_aficionado():
    cust1 = Customer("Alvin")
    cust2 = Customer("Sean")
    coffee = Coffee("Galao")

    cust1.create_order(coffee, 5.0)
    cust1.create_order(coffee, 6.0)
    cust2.create_order(coffee, 7.0)

    result = Customer.most_aficionado(coffee)
    assert result.name == cust1.name

    coffee2 = Coffee("Americano")
    assert Customer.most_aficionado(coffee2) is None
