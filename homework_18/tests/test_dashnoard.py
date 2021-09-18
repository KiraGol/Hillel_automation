import time


def test_check_choose_category_of_product(dashboard):
    dashboard.choose_category("Портативная техника")
    product_list_page = dashboard.choose_subcategory("Ноутбуки")
    time.sleep(3)
    product_page = product_list_page.choose_first_product()
    time.sleep(3)


def test_check_search_field_works(dashboard):
    dashboard.input_text_in_search_field_and_find_product("Ноутбуки")
    time.sleep(3)


def test_scroll_to_element(dashboard):
    dashboard.scroll_to_element_contact_us()
    time.sleep(3)
