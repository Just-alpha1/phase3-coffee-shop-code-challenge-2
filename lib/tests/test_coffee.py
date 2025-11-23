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
