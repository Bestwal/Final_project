
import time
from main_str import MainStr
from locate import  Links


def test_add_to_basket(browser):
    page = MainStr(browser, Links.MAIN_LINK)
    page.open()
    page.click_to_add_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)

