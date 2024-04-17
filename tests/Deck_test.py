import pytest
from lib.Deck import Deck
from lib.Card import Card


class TestDeck:

    def test_deck_initialises_with_52_cards(self):
        deck = Deck()
        assert len(deck) == 52

    def test_draw_one_card(self):
        deck = Deck()
        assert deck.draw() == Card("Ace", "Clubs")
        assert len(deck) == 51

    def test_draw_two_cards(self):
        deck = Deck()
        assert deck.draw() == Card("Ace", "Clubs")
        assert deck.draw() == Card(2, "Clubs")
        assert len(deck) == 50

    def test_draw_two_cards_simulanteously(self):
        deck = Deck()
        assert deck.draw(2) == [Card("Ace", "Clubs"), Card(2, "Clubs")]
        assert len(deck) == 50

    def test_two_new_decks_are_equal(self):
        deck1 = Deck()
        deck2 = Deck()
        assert deck1 == deck2

    def test_deck_is_shuffled(self):
        unshuffled_deck = Deck()
        shuffled_deck = Deck()
        shuffled_deck.shuffle_deck()
        assert unshuffled_deck != shuffled_deck
        assert len(shuffled_deck) == 52

    def test_cannot_draw_cards_when_deck_empty(self):
        deck = Deck()
        deck.draw(52)
        assert len(deck) == 0
        with pytest.raises(Exception) as e:
            deck.draw()
        assert str(e.value) == "There are not enough cards left!"

    def test_cannot_draw_53_cards(self):
        deck = Deck()
        with pytest.raises(Exception) as e:
            deck.draw(53)
        assert str(e.value) == "There are not enough cards left!"
