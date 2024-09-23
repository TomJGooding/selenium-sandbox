from pages.webform import WebFormPage
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def test_webform() -> None:
    driver = setup()

    driver.implicitly_wait(0.5)

    webform_page = WebFormPage(driver)
    webform_page.load()

    webform_page.type_text_input("Selenium")
    form_submitted_page = webform_page.click_submit()

    assert form_submitted_page.get_message_text() == "Received!"

    teardown(driver)


def setup() -> WebDriver:
    driver = webdriver.Chrome()
    return driver


def teardown(driver: WebDriver) -> None:
    driver.quit()
