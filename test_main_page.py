import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                                         # открываем страницу
        page.go_to_login_page()                             # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # выполняем метод страницы - переходим на страницу логина
        login_page.should_be_login_page()                   # реализация теста

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()             # реализация теста

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"  
    page = BasketPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес             
    page.open()                             # Гость открывает главную страницу 
    page.go_to_basket()                     # Переходит в корзину по кнопке в шапке сайта
    page.should_in_basket_not_item()        # Проверяем, что в корзине нет товара
    page.should_basket_is_empty()           # Проверяем, что корзина пустая (имеется текст "empty")

    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.go_to_login_page()             # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

