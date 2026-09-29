from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self, url):

        self.driver.get(url)

    def login(self, username, password):

        self.type(self.USERNAME, username)

        self.type(self.PASSWORD, password)

        self.click(self.LOGIN)

    def error_message(self):

        return self.text(self.ERROR)
