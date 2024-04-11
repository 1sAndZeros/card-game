from lib.Card import Card


class TestCard:

    def test_card_initialises(self):
        card = Card("Ace", "Spades")
        assert card.face_value == "Ace"
        assert card.suit == "Spades"
        assert card.value == 1

    def test_card_prints_correctly(self):
        card = Card("Ace", "Spades")
        assert str(card) == "Ace of Spades"

    def test_two_cards_are_equal(self):
        card1 = Card("Ace", "Spades")
        card2 = Card("Ace", "Spades")
        assert card1 == card2

    def test_two_cards_are_not_equal(self):
        card1 = Card(2, "Spades")
        card2 = Card("Ace", "Spades")
        assert card1 != card2
