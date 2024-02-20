from Cards import Deck
from Cards import Card
from typing import List

@staticmethod
class DealerFunctions:

    def getDealerCards(deck: Deck) -> List[Card]:
        card1, card2 = deck.drawCards(2)
        hand = [card1, card2]
        return hand