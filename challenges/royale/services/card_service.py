from typing import List

import requests

from royale.models.card import Card


# def get_all_cards() -> List[Card]:
#     response = requests.get('https://statsroyale.com/api/cards')
#     if response.ok:
#         return [Card(**card) for card in response.json()]
#
#     else:
#         raise Exception('Response was not ok.  Status Code: ' + response.status_code)


def get_all_cards() -> List[Card]:
    response = requests.get('https://statsroyale.com/api/cards')
    if response.ok:
        cards = [Card(**card) for card in response.json()]

        # Since the API comes back with types as follows:
        # tid_card_type_building
        # tid_card_type_spell
        # tid_card_type_character
        # We do this to convert them to what actually comes up on the front end.
        # In a real test environment this would be a bug and either the front end or the back end would need to change
        # We just change it currently to get our tests to pass which is not good.
        # Another bug is the API gives you arena 0 but the front end gives you training camp
        for card in cards:
            if "spell" in card.type:
                card.type = "Spell"
            elif "building" in card.type:
                card.type = "Building"
            else:
                card.type = "Troop"

        return cards


def get_card_by_name(card_name: str) -> Card:
    cards = get_all_cards()
    return next(card for card in cards if card.name == card_name)

