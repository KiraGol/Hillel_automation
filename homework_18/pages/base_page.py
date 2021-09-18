from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework_18.core.locator import Locator


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)
        self.action = ActionChains(driver)

    def _wait_until_element_appears(self, locator: Locator) -> WebElement:
        return self.__web_driver_wait.until(
            EC.presence_of_element_located(locator.to_tuple())
        )

    def _click(self, locator: Locator) -> None:
        self._wait_until_element_appears(locator).click()

    def _move_to_element(self, target_element) -> None:
        self.action.move_to_element(target_element).click().perform()



