from lib.Card import Card
from lib.values import suits, lookup
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.create_new_deck()

    def __len__(self):
        return len(self.cards)

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__

    def create_new_deck(self):
        for suit in suits:
            for value in lookup.keys():
                self.cards.append(Card(value, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw(self, number=1):
        cards = []
        for _ in range(number):
            cards.append(self.cards.pop(0))
        return cards[0] if len(cards) == 1 else cards
