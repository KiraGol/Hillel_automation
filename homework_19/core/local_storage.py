from homework_19.core.web_driver import WebDriver


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def _my_add_local_storage(self, key, value):
        self.__driver.execute_script(f"window.localStorage['{key}'] = '{value}'")

    def _my_get_local_storage(self):
        print(self.__driver.execute_script("return window.localStorage;"))

    def _my_get_some_in_local_storage(self, key):
        print(self.__driver.execute_script(f"return window.localStorage['{key}'];"))
