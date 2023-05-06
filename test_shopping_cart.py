from shopping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")

    assert cart.size() == 1


def test_can_get_items():
    pass


def test_can_get_total_price():
    pass


def test_when_item_added_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_cart_is_more_than_max():
    cart = ShoppingCart(5)
    with pytest.raises(OverflowError):
        for i in range(6):
            cart.add("apple")

    pass

