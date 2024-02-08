from Cards import Deck

deck = Deck()

all_cards = [str(card.getValue().name) + " OF " + str(card.getSuit().name) for card in deck.getCards()]

for card_name in all_cards:
    print(card_name)