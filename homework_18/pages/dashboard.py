import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from homework_18.core.locator import Locator
from homework_18.core.page_singleton import singleton
from homework_18.pages.base_page import BasePage

from homework_18.pages.product_list_page import ProductListPage


@singleton
class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def choose_category(self, name: str) -> None:
        self._click(Locator(By.XPATH, f"//span[contains(text(),'{name}')][1]"))

    def choose_subcategory(self, name: str) -> ProductListPage:
        self._click(Locator(By.XPATH, f"//a[@class='link'][contains(text(),'{name}')]"))
        return ProductListPage(self._driver)

    def input_text_in_search_field_and_find_product(self, text: str):
        search_input_field_element: WebElement = self._driver.find_element(By.XPATH, f"//input[@id='search-input']")
        search_input_field_element.send_keys(f"{text}")
        search_button_element: WebElement = self._driver.find_element(By.XPATH, f"//button[@class='search-btn']")
        search_button_element.click()

    def scroll_to_element_contact_us(self) -> None:
        target_element: WebElement = self._driver.find_element(By.XPATH, f"//span[contains(text(),'Связь с нами')]")
        self._move_to_element(target_element)


