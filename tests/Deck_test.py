from lib.Deck import Deck
from lib.Card import Card


class TestDeck:

    def test_deck_initialises_with_52_cards(self):
        deck = Deck()
        assert len(deck) == 52

    def test_draw_one_card(self):
        deck = Deck()
        assert deck.draw() == Card("Ace", "Clubs")

    def test_draw_two_cards(self):
        deck = Deck()
        assert deck.draw() == Card("Ace", "Clubs")
        assert deck.draw() == Card(2, "Clubs")

    def test_draw_two_cards_simulanteously(self):
        deck = Deck()
        assert deck.draw(2) == [Card("Ace", "Clubs"), Card(2, "Clubs")]

    def test_two_new_decks_are_equal(self):
        deck1 = Deck()
        deck2 = Deck()
        assert deck1 == deck2

    def test_deck_is_shuffled(self):
        unshuffled_deck = Deck()
        shuffled_deck = Deck()
        shuffled_deck.shuffle_deck()
        assert unshuffled_deck != shuffled_deck
