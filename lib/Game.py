import inquirer
import re
import random
from lib.Deck import Deck
from lib.Player import Player
from lib.Card import Card
from utils import clear
from time import sleep


class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = players[0]
        self.deck.deal(players)
        self.game_over = False
        self.trick: list[tuple[Player, Card]] = []
        self.tricks = []

    def start_game(self):
        while not self.game_over:
            clear()
            self.print_scores()
            self.trick = []

            for player in self.players[::-1]:
                card_played = self.play_card(player)
                self.trick.append((player, card_played))
                sleep(0.5)

            self.check_trick_winner(card_played)
            self.tricks.append(self.trick)
            self.check_game_over()

    def play_card(self, player: Player):
        hand = player.hand
        leading_card = None

        if len(self.trick) > 0:
            leading_card = self.trick[0]

        choices = [
            (i, card)
            for i, card in enumerate(hand)
            if not leading_card or card.suit == leading_card[1].suit
        ]

        if len(choices) == 0:
            choices = [(i, card) for i, card in enumerate(hand)]

        if player.id == 1:
            card_played_idx = None
            choices = [f"{i + 1}" + "\t" + str(card) for i, card in choices]
            questions = [
                inquirer.List(
                    "card",
                    message="Pick a card to play?",
                    choices=choices,
                    carousel=True,
                ),
            ]
            answers = inquirer.prompt(questions)
            choice = re.match(r"\d+", answers["card"]).group()
            card_played_idx = int(choice) - 1
        else:
            card_played_idx = random.choice(choices)[0]

        return player.play_card(card_played_idx)

    def check_trick_winner(self, trick):
        winning_player = None
        max_card = -1
        for player, card in self.trick:
            if card.value > max_card:
                max_card = card.value
                winning_player = player

        print(
            f"{'You' if winning_player.id == 1 else winning_player.name} won this hand"
        )
        winning_player.score += 1
        sleep(3)

    def print_scores(self):
        for player in self.players:
            print(f"{player.name} scored: {player.score}")

    def check_game_over(self):
        if len(self.player1.hand) == 0:
            self.game_over = True

        print(
            """------------
Game Over
------------"""
        )
        self.print_scores()
