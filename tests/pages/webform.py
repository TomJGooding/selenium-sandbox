from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base import BasePage


class WebFormPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def load(self) -> None:
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    def type_text_input(self, value: str) -> None:
        text_box = self.driver.find_element(By.NAME, "my-text")
        text_box.send_keys(value)

    def click_submit(self) -> None:
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button")
        submit_button.click()
