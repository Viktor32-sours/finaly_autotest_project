from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_add_button()
        self.should_be_price_product()
        self.should_be_name_product()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.correct_product_name_on_basket()
        self.correct_product_price_on_basket()
        


    def should_be_product_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_LINK), "Button add product is not presented" 

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_LINK), "Product price is not presented"

    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_LINK), "Product name is not presented" 


    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        button.click()


    def correct_product_name_on_basket(self):
        name_page_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_LINK)
        name_on_basket_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ON_BASKET_LINK)
        assert name_page_product.text == name_on_basket_product.text,"Name for added product no correct product on basket "
       

    def correct_product_price_on_basket(self):
        price_page_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_LINK)
        price_on_basket_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ON_BASKET_LINK)
        assert price_page_product.text == price_on_basket_product.text, "Price for added product no correct price on basket "
       

    


    