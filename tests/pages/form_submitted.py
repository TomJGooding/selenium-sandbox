from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base import BasePage


class FormSubmittedPage(BasePage):
    # Locators
    MESSAGE = (By.ID, "message")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def load(self) -> None:
        raise NotImplementedError

    def get_message_text(self) -> str:
        message = self.driver.find_element(*self.MESSAGE)
        return message.text
