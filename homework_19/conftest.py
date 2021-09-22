import time

from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from homework_18.pages.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("../driver/chromedriver")
    driver.maximize_window()
    driver.get("https://qwertyshop.ua/")
    time.sleep(3)

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver) -> Dashboard:
    yield Dashboard(driver)
