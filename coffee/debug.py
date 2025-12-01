# debbug.py
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def run_debug_tests():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Create orders
    order1 = alice.create_order(espresso, 3.5)
    order2 = bob.create_order(espresso, 4.0)
    order3 = alice.create_order(latte, 5.0)
    order4 = bob.create_order(latte, 4.5)
    order5 = alice.create_order(espresso, 3.8)

    # Display orders for each customer
    print(f"{alice.name}'s orders: {[f'{o.coffee.name} at ${o.price}' for o in alice.orders()]}")
    print(f"{bob.name}'s orders: {[f'{o.coffee.name} at ${o.price}' for o in bob.orders()]}")

    # Display coffees ordered by Alice
    print(f"Coffees ordered by {alice.name}: {[coffee.name for coffee in alice.coffees()]}")

    # Display customers for Espresso coffee
    print(f"Customers who ordered {espresso.name}: {[customer.name for customer in espresso.customers()]}")

    # Display number of orders and average price for Espresso
    print(f"Number of orders for {espresso.name}: {espresso.num_orders()}")
    print(f"Average price for {espresso.name}: ${espresso.average_price():.2f}")

    # Display most aficionado customer for Latte
    most_aficionado = Customer.most_aficionado(latte)
    if most_aficionado:
        print(f"Most aficionado for {latte.name}: {most_aficionado.name}")
    else:
        print(f"No orders found for {latte.name}")

if _name_ == "_main_":
    run_debug_tests()