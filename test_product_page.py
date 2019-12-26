import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.email = str(time.time()) + "@fakemail.org" 
        self.password = str(time.time()//2)
        self.page.register_new_user(self.email, self.password)
        self.page.should_be_authorized_user()
        
        # yield # "yield" писать не нужно — пользователей удалять мы не умеем
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        # self.product.delete()  # 

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)                # Создаем объект ProductPage         
        page.open()                                      # Открываем страницу товара
        page.should_not_be_success_message()             # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                                   # открываем страницу
        page.should_be_product_page()                 # Проверяем страницу товара

  

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                              # открываем страницу
    page.should_be_product_page()            # проверка страницы товара

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",  marks=pytest.mark.xfail)])    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)                       
    page.open()                                     # Открываем страницу товара
    page.add_product_to_basket()                    # Добавляем товар в корзину
    page.solve_quiz_and_get_code()                  # Заполняем капчу 
    page.should_not_be_success_message()            # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]) 
def test_guest_cant_see_success_message(browser, link): 
    page = ProductPage(browser, link)           # Создаем объект ProductPage         
    page.open()                                 # Открываем страницу товара
    page.should_not_be_success_message()        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    
    

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", marks=pytest.mark.xfail),
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9", marks=pytest.mark.xfail)]) 
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)                       
    page.open()                               # Открываем страницу товара
    page.add_product_to_basket()              # Добавляем товар в корзину       
    page.solve_quiz_and_get_code()            # Заполняем капчу 
    page.should_disappear_success_message()   # Проверяем, что  сообщения об успехе исчезает с помощью is_disappeared
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"  
    page = BasketPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес             
    page.open()                             # Гость открывает страницу товара
    page.go_to_basket()                     # Переходит в корзину по кнопке в шапке сайта
    page.should_in_basket_not_item()        # Проверяем, что в корзине нет товара
    page.should_basket_is_empty()           # Проверяем, что корзина пустая (имеется текст "empty")
