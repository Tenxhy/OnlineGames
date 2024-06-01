from Cards import Deck
from Cards import Suit
from Cards import Value
from Cards import Card

card1 = Card(Value.JACK, Suit.SPADES)
card1.display()
print(f"{card1.getValue()=} {card1.getValueInt()=}")
card2 = Card(Value.SEVEN, Suit.HEARTS)
card2.display()