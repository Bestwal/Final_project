from base import BasePage
from locate import Locators, Links

class MainStr(BasePage):
    def  click_to_add_basket(self):
        button = self.browser.find_element(*Locators.ADD_BASKET_BUTTON)
        button.click()

