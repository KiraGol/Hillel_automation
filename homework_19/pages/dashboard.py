from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework_18.core.page_singleton import singleton
from homework_18.pages.base_page import BasePage

from homework_18.pages.product_list_page import ProductListPage


@singleton
class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def choose_category(self, name: str) -> None:
        self._click((By.XPATH, f"//span[contains(text(),'{name}')][1]"))

    def choose_subcategory(self, name: str) -> ProductListPage:
        self._click((By.XPATH, f"//a[@class='link'][contains(text(),'{name}')]"))
        return ProductListPage(self._driver)
