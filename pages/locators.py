from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTOM_LINK = (By.CSS_SELECTOR , "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_EMPTY_LINK =(By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEM_LINK = (By.CSS_SELECTOR,".basket-items")

class LoginPageLocators():
    REGISTER_FORM_LINK = (By.ID, "register_form")
    LOGIN_FORM_LINK = (By.ID, "login_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BASKET_VIEW_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    NAME_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    NAME_PRODUCT_ON_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    PRICE_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_PRODUCT_ON_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR , "#messages > div:nth-child(1) > div")



