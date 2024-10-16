import json

import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):
    with open("tests/config.json") as f:
        config = json.load(f)

    assert config["driver"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], (int, float))
    assert config["implicit_wait"] > 0

    return config


@pytest.fixture
def driver(config):
    if config["driver"] == "Firefox":
        driver = selenium.webdriver.Firefox()
    elif config["driver"] == "Chrome":
        driver = selenium.webdriver.Chrome()
    elif config["driver"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Driver '{config['driver']}' is not supported")

    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    driver.quit()
