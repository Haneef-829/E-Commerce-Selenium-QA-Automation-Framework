from config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_cart_contains_product(driver):

    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    products = ProductsPage(driver)

    products.add_backpack()

    products.open_cart()

    cart = CartPage(driver)

    assert cart.title() == "Your Cart"

    assert cart.item_count() == 1
