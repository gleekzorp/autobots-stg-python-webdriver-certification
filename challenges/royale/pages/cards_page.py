from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CardsPage:
    def __init__(self, driver: WebDriver):
        self.map = CardsPageMap(driver)

    def goto(self):
        self.map.cards_link().click()

    def get_card_by_name(self, card_name: str) -> WebElement:
        if " " in card_name:
            card_name = card_name.replace(" ", "+")
        return self.map.card(card_name)


class CardsPageMap:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def cards_link(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "a[href='/cards']")

    def card(self, card_name) -> WebElement:
        """ Gets the card on the page given the card name

        :param card_name: the card name
        :return: The card as a WebElement
        """
        return self._driver.find_element(By.CSS_SELECTOR, f"a[href*='/{card_name}']")