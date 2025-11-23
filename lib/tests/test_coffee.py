import pytest
from lib.classes.coffee import Coffee
from lib.classes.customer import Customer

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")

    c = Coffee("Cappuccino")
    assert c.name == "Cappuccino"
    c.name = "Red eye"
    assert c.name == "Red eye"
    with pytest.raises(ValueError):
        c.name = "ab"
def test_orders_customers_num_orders_average_price():
    cust1 = Customer("Alvin")
    cust2 = Customer("Sean")
    coffee = Coffee("Galao")

    order1 = cust1.create_order(coffee, 5.0)
    order2 = cust2.create_order(coffee, 7.0)

    orders = coffee.orders()
    customers = coffee.customers()
    num_orders = coffee.num_orders()
    avg_price = coffee.average_price()

    assert order1 in orders
    assert order2 in orders
    assert cust1 in customers
    assert cust2 in customers
    assert num_orders == 2
    assert avg_price == 6.0
