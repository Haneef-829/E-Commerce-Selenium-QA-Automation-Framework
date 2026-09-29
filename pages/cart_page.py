from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")

    ITEMS = (By.CLASS_NAME, "cart_item")

    CHECKOUT = (By.ID, "checkout")

    def title(self):

        return self.text(self.TITLE)

    def item_count(self):

        return len(
            self.driver.find_elements(*self.ITEMS)
        )

    def checkout(self):

        self.click(self.CHECKOUT)
