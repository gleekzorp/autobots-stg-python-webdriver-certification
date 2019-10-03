import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.pages import Pages


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get("https://www.statsroyale.com")
    pages = Pages(driver)
    yield pages
    driver.quit()


# card_names = ['Ice Spirit', 'Mirror', 'Lava Hound']
card_names = ['Ice Spirit']


@pytest.mark.parametrize('card_name', card_names)
def test_card_is_displayed(royale, card_name):
    royale.cards.goto()
    card = royale.cards.get_card_by_name(card_name)
    assert card.is_displayed


@pytest.mark.parametrize('card_name', card_names)
def test_details_are_correct(royale, card_name):
    royale.cards.goto()
    royale.cards.get_card_by_name(card_name).click()

    card_name_on_page = royale.card_detail.map.card_name.text
    card_deets = royale.card_detail.map.card_deets.text.split(', ')
    card_type = card_deets[0]
    card_arena = card_deets[1]
    card_rarity = royale.card_detail.map.card_rarity.text

    assert card_name_on_page == card_name
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'


# Original
# def test_details_are_correct(driver):
#     cards_link = driver.find_element(By.CSS_SELECTOR, "a[href='/cards']")
#     cards_link.click()
#
#     ice_spirit = driver.find_element(By.CSS_SELECTOR, "a[href*='Ice+Spirit']")
#     ice_spirit.click()
#
#     card_name = driver.find_element(By.CSS_SELECTOR, "[class*='ui__headerMedium card__cardName']").text
#     card_deets = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(', ')
#     card_type = card_deets[0]
#     card_arena = card_deets[1]
#     card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='card__count']").text
#     assert card_name == 'Ice Spirit'
#     assert card_type == 'Troop'
#     assert card_arena == 'Arena 8'
#     assert card_rarity == 'Common'