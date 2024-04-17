from lib.Card import Card


class Player:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name.title()
        self.hand: list[Card] = []
        self.score: int = 0

    def __repr__(self) -> str:
        return f"Player {self.id} - {self.name}"

    def __eq__(self, value: object) -> bool:
        return self.id == value.id and self.name == value.name

    def add_cards_to_hand(self, card: Card):
        self.hand.append(card)

    def see_hand(self):
        if len(self.hand) == 0:
            return "You have no cards left"

        cards = [str(card) + "\n" for card in self.hand]
        return f"""------------------------
You have the following cards in your hand:
{''.join(cards)}------------------------"""

    def play_card(self, hand_index: int):
        if hand_index < 0 or hand_index >= len(self.hand):
            raise Exception("Sorry, cannot find that card")
        card = self.hand.pop(hand_index)
        print(f"{'You' if self.id == 1 else self.name} played: {card}")
        return card
