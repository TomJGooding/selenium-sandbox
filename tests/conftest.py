import pytest
import selenium.webdriver


@pytest.fixture
def driver():
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(0.5)

    yield driver

    driver.quit()
