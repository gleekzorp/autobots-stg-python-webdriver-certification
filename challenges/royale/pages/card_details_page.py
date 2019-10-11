from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.models.card import Card


class CardDetailsPage:
    def __init__(self, driver):
        self.map = CardDetailsPageMap(driver)

    def get_base_card(self) -> Card:
        type_and_arena = self.get_card_type_and_arena()
        return Card(
            id=0,
            cost=0,
            icon=None,
            name=self.map.card_name.text,
            type=type_and_arena[0],
            arena=type_and_arena[1],
            rarity=self.map.card_rarity.text
        )

    def get_card_type_and_arena(self) -> Tuple[str, int]:
        type_and_arena = self.map.card_deets.text.split(', ')
        card_type = type_and_arena[0]
        card_arena = type_and_arena[1].split(' ')[-1]
        return card_type, int(card_arena)


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

