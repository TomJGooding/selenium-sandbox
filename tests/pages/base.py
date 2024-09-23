from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(ABC):
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError
