from lib.Player import Player


class TestPlayer:

    def test_player_initialises(self):
        player = Player(1, "rikie")
        assert player.id == 1
        assert player.name == "Rikie"
        assert not player.hand

    def test_player_prints_correctly(self):
        player = Player(1, "rikie patrick")
        assert str(player) == "Player 1 - Rikie Patrick"

    def test_two_players_are_equal(self):
        player1 = Player(1, "rikie patrick")
        player1_clone = Player(1, "rikie patrick")
        assert player1 == player1_clone

    def test_two_players_are_not_equal(self):
        player1 = Player(1, "rikie patrick")
        player2 = Player(2, "rikie patrick")
        assert player1 != player2

    def test_player_see_empty_hand(self):
        player1 = Player(1, "rikie patrick")
        assert player1.see_hand() == "You have no cards left"
