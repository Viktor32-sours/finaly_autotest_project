from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_basket_page(self):
        self.should_button_basket()
        self.should_basket_is_empty() 
        self.should_in_basket_not_item()

    def go_to_basket(self):
        self.should_button_basket()
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTOM_LINK)
        button.click()

    def should_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_LINK), "Basket is not empty"
        
    def should_button_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTOM_LINK), "Button 'View basket' is not presented"

    def should_in_basket_not_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_LINK), "Button 'View basket' is not presented"

   


