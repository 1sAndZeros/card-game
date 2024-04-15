from lib.Card import Card
from lib.values import suits, values
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
            for value in values.keys():
                self.cards.append(Card(value, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw(self, number=1):
        cards = []

        if number > len(self):
            raise Exception("There are not enough cards left!")

        for _ in range(number):
            cards.append(self.cards.pop(0))
        return cards[0] if len(cards) == 1 else cards

    def deal(self, players):
        cards_dealt = 0
        while len(self.cards) >= len(players):
            for player in players:
                player.add_cards_to_hand(self.draw())
            cards_dealt += 1
        print(f"{cards_dealt} cards dealt to each player")
        print(f"{len(self)} cards remaining")
