from homework_19.core.web_driver import WebDriver


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def _my_add_cookie(self, values):
        self.__driver.add_cookie(f"{values}")

    def _my_get_cookie(self, value):
        self.__driver.get_cookie(f"{value}")

    def _my_del_cookie(self, name):
        self.__driver.delete_cookie(f"{name}")

