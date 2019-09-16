from selenium.webdriver.remote.webdriver import WebDriver

from royale.pages.cards_page import CardsPage


class Pages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cards = CardsPage(driver)
