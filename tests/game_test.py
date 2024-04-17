from lib.Game import Game
from lib.Player import Player
from lib.Deck import Deck
from lib.Card import Card
import pytest


class TestGame:

    def test_game_initialises_correctly(self):
        players = [Player(1, "Rikie"), Player(2, "Computer")]
        game = Game(players)
        assert len(game.players) == 2
        assert not game.deck == Deck()
        assert game.player1 == Player(1, "Rikie")
        assert len(game.player1.hand) == 26
        assert game.game_over == False
        assert game.trick == []
        assert game.tricks == []
        assert game.previous_winner == None

    def test_print_scores(self, capsys):
        players = [Player(1, "Rikie"), Player(2, "Computer")]
        game = Game(players)
        game.print_scores()
        captured = capsys.readouterr()
        assert "Rikie" in captured.out

    # @pytest.mark.skip(reason="Too slow")
    def test_game_over(self):
        players = [Player(1, "Rikie"), Player(2, "Computer")]
        game = Game(players)
        for i in range(26):
            game.player1.play_card(0)
        game.check_game_over()
        assert game.game_over == True

    def test_check_winner(self):
        players = [Player(1, "Rikie"), Player(2, "Computer")]
        game = Game(players)
        game.player1.score = 999
        assert game.check_winner() == [Player(1, "Rikie")]

    def test_trick_winner_same_suit(self):
        player1 = Player(1, "Rikie")
        computer = Player(2, "Computer")
        players = [player1, computer]
        game = Game(players)
        high_card = Card(10, "Clubs")
        low_card = Card(3, "Clubs")
        winner = game.check_trick_winner([(player1, low_card), (computer, high_card)])
        assert winner == computer
        assert computer.score == 1

    def test_trick_winner_when_no_others_follow_suit(self):
        player1 = Player(1, "Rikie")
        computer = Player(2, "Computer")
        players = [player1, computer]
        game = Game(players)
        high_card = Card(10, "Hearts")
        low_card = Card(3, "Clubs")
        winner = game.check_trick_winner([(player1, low_card), (computer, high_card)])
        assert winner == player1
        assert player1.score == 1

    def test_check_winner(self):
        player1 = Player(1, "Rikie")
        computer = Player(2, "Computer")
        players = [player1, computer]
        game = Game(players)
        player1.score = 99
        computer.score = 0
        winners = game.check_winner()
        assert winners == [player1]
        player1.score = 5
        computer.score = 12
        winners = game.check_winner()
        assert winners == [computer]
        player1.score = 52
        computer.score = 52
        winners = game.check_winner()
        assert winners == [player1, computer]
