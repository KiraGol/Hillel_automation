from homework_18.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self) -> str:
        pass
