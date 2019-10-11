import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.card_details_page import CardDetailsPage
from royale.pages.pages import Pages
from royale.services import card_service


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get("https://www.statsroyale.com")
    pages = Pages(driver)
    yield pages
    driver.quit()


# card_names = ['Ice Spirit', 'Mirror', 'Lava Hound']
card_names = ['Ice Spirit']

cards = card_service.get_all_cards()


@pytest.mark.parametrize('api_card', cards)
def test_card_is_displayed(royale, api_card):
    royale.cards.goto()
    card_on_page = royale.cards.get_card_by_name(api_card.name)
    assert card_on_page.is_displayed


# Before change
# @pytest.mark.parametrize('card_name', card_names)
# def test_card_is_displayed(royale, card_name):
#     royale.cards.goto()
#     card = royale.cards.get_card_by_name(card_name)
#     assert card.is_displayed

@pytest.mark.parametrize('api_card', cards)
def test_details_are_correct(royale, api_card):
    royale.cards.goto()
    royale.cards.get_card_by_name(api_card.name).click()

    card = royale.card_detail.get_base_card()

    assert card.name == api_card.name
    # assert card.type == api_card.get_type(api_card.type)
    assert card.type == api_card.type
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity

# Before change
# @pytest.mark.parametrize('card_name', card_names)
# def test_details_are_correct(royale, card_name):
#     royale.cards.goto()
#     royale.cards.get_card_by_name(card_name).click()
#
#     card = royale.card_detail.get_base_card()
#
#     assert card.name == card_name
#     assert card.type == 'Troop'
#     assert card.arena == 8
#     assert card.rarity == 'Common'


def test_ice_spirit_is_not_displayed(royale):
    royale.cards.goto()
    royale.driver.find_element(By.ID, "common-cards").click()

    ice_spirit_card = royale.driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")

    assert ice_spirit_card.is_displayed() is False


