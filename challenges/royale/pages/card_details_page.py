from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CardDetailsPage:
    def __init__(self, driver):
        self.map = CardDetailsPageMap(driver)


class CardDetailsPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    @property
    def card_deets(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']")

    @property
    def card_rarity(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__count']")

