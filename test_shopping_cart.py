from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")

    assert cart.size() == 1


def test_can_get_items(cart):
    cart.add("apple")
    cart.add("orange")

    price_map = {
        "apple": 1.0,
        "orange": 2.0,
    }
    assert cart.get_total_price(price_map) == 3.0


def test_can_get_total_price(cart):
    print("Testing can get price")
    pass


def test_when_item_added_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_cart_is_more_than_max(cart):
    for i in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")
