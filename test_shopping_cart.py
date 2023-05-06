from unittest.mock import Mock

import item_database
from item_database import ItemDatabase
from shopping_cart import ShoppingCart
import pytest


@pytest.fixture
# setup for the cart, reduces code duplication
def cart():
    return ShoppingCart(5)


@pytest.fixture
def database():
    return ItemDatabase()


def test_can_add_item_to_cart(cart):
    cart.add("apple")

    assert cart.size() == 1


def test_can_get_total_price(cart, database):
    cart.add("apple")
    cart.add("orange")

    # price_map = {
    #     "apple": 1.0,
    #     "orange": 2.0,
    # }
    # replace instance of item database with price map
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item())
    assert cart.get_total_price(item_database) == 3.0


def test_when_item_added_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_cart_is_more_than_max(cart):
    for i in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")
