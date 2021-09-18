from selenium.webdriver.common.by import By

from homework_18.core.locator import Locator
from homework_18.pages.base_page import BasePage
from homework_18.pages.product_page import ProductPage


class ProductListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__first_product_locator = Locator(By.XPATH, "//a[@class='product-block-name-link'][1]")

    def choose_first_product(self) -> ProductPage:
        self._click(self.__first_product_locator)
        return ProductPage(self._driver)