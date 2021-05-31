from pages.main_page import MainPage


def test_should_be_register_legal(browser):
    link = "https://advert.demo.notamedia.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_legal()


def test_should_be_approval_of_the_application(browser):
    link = "https://backend.advert.demo.notamedia.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_approval_of_the_application()


def test_should_be_authorization(browser):
    link = "https://advert.demo.notamedia.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_authorization()


def test_should_be_add_campaign(browser):
    link = "https://advert.demo.notamedia.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_add_campaign()
