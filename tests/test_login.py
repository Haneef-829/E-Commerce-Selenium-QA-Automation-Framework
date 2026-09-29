from config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD
)

from pages.login_page import LoginPage

from pages.products_page import ProductsPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    products = ProductsPage(driver)

    assert products.title() == "Products"


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login(
        INVALID_USERNAME,
        INVALID_PASSWORD
    )

    assert "Username and password do not match" in \
        login.error_message()
