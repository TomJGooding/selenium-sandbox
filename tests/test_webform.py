from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_webform() -> None:
    driver = setup()

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(By.NAME, "my-text")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(By.ID, "message")
    value = message.text

    assert value == "Received!"

    teardown(driver)


def setup() -> WebDriver:
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver


def teardown(driver: WebDriver) -> None:
    driver.quit()
