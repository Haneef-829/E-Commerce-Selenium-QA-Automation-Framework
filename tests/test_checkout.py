from config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage

from pages.checkout_page import CheckoutPage


def test_complete_checkout(driver):

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

    cart.checkout()

    checkout = CheckoutPage(driver)

    checkout.enter_customer_details(
        "Sarath",
        "Babu",
        "517325"
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert checkout.confirmation() == \
        "Thank you for your order!"
