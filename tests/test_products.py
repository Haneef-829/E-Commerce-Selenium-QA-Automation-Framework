from config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage

from pages.products_page import ProductsPage


def login(driver):

    page = LoginPage(driver)

    page.open(BASE_URL)

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )


def test_product_page(driver):

    login(driver)

    products = ProductsPage(driver)

    assert products.title() == "Products"


def test_products_are_displayed(driver):

    login(driver)

    products = ProductsPage(driver)

    assert products.product_count() > 0


def test_add_product_to_cart(driver):

    login(driver)

    products = ProductsPage(driver)

    products.add_backpack()

    products.open_cart()
