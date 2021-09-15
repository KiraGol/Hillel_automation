import time

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement


def test_number_one():
    driver = Chrome("./driver/chromedriver")
    search_input_field_locator = "//input[@title='Поиск']"
    first_search_result_locator = "//ul[@role='listbox']//li[1]"
    link_in_search_result_locator = "//div[@class='TbwUpd NJjxre']//cite[1]"

    driver.get("https://google.com")
    search_input_field: WebElement = driver.find_element_by_xpath(search_input_field_locator)
    search_input_field.send_keys("Qwertyshop")
    time.sleep(3)
    first_search_result_element: WebElement = driver.find_element_by_xpath(first_search_result_locator)
    first_search_result_element.click()
    time.sleep(3)
    link_in_search_result: WebElement = driver.find_element_by_xpath(link_in_search_result_locator)
    link_in_search_result.click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


    driver.quit()
