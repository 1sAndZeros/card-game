from lib.Player import Player
from lib.Card import Card
import pytest


class TestPlayer:

    def test_player_initialises(self):
        player = Player(1, "rikie")
        assert player.id == 1
        assert player.name == "Rikie"
        assert not player.hand
        assert player.score == 0

    def test_player_prints_correctly(self):
        player = Player(1, "rikie patrick")
        assert str(player) == "Player 1 - Rikie Patrick"

    def test_two_players_are_equal(self):
        player1 = Player(1, "rikie patrick")
        player1_clone = Player(1, "rikie patrick")
        assert player1 == player1_clone
        player1_clone.add_cards_to_hand(Card(2, "Clubs"))
        assert player1 == player1_clone

    def test_two_players_are_not_equal(self):
        player1 = Player(1, "rikie patrick")
        player2 = Player(2, "rikie patrick")
        assert player1 != player2

    def test_player_see_empty_hand(self):
        player1 = Player(1, "rikie patrick")
        assert player1.see_hand() == "You have no cards left"

    def test_add_cards_to_hand(self):
        player1 = Player(1, "rikie patrick")
        player1.add_cards_to_hand(Card(3, "Clubs"))
        assert Card(3, "Clubs") in player1.hand
        player1.add_cards_to_hand(Card(4, "Hearts"))
        assert str(Card(4, "Hearts")) in player1.see_hand()

    def test_play_card(self):
        player1 = Player(1, "rikie patrick")
        player1.add_cards_to_hand(Card(3, "Clubs"))
        player1.add_cards_to_hand(Card(4, "Hearts"))
        player1.play_card(0)
        assert Card(3, "Clubs") not in player1.hand
        assert Card(4, "Hearts") in player1.hand

    def test_play_card_index_out_of_range(self):
        player1 = Player(1, "rikie patrick")
        player1.add_cards_to_hand(Card(3, "Clubs"))
        player1.add_cards_to_hand(Card(4, "Hearts"))
        with pytest.raises(Exception) as e:
            player1.play_card(2)
        assert str(e.value) == "Sorry, cannot find that card"
