from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")

    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    CART = (By.CLASS_NAME, "shopping_cart_link")

    ADD_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    def title(self):

        return self.text(self.TITLE)

    def product_count(self):

        return len(
            self.driver.find_elements(*self.PRODUCTS)
        )

    def add_backpack(self):

        self.click(self.ADD_BACKPACK)

    def open_cart(self):

        self.click(self.CART)
