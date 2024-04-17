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
        self.previous_winner: None | Player = None

    def start_game(self):

        random.shuffle(self.players)

        while not self.game_over:
            self.print_scores()
            self.trick = []

            self.set_starting_player()

            for i, player in enumerate(self.players):
                card_played = None
                if len(self.tricks) == 0 and i == 0:
                    for j, card in enumerate(player.hand):
                        if card == Card(2, "Clubs"):
                            card_played = player.play_card(j)
                            break
                else:
                    card_played = self.play_card(player)
                self.trick.append((player, card_played))

            self.previous_winner = self.check_trick_winner(self.trick)
            self.tricks.append(self.trick)
            self.check_game_over()

    def set_starting_player(self):
        for player in self.players:

            has_2_clubs = Card(2, "Clubs") in player.hand
            is_prev_winner = self.previous_winner and player == self.previous_winner

            if has_2_clubs or is_prev_winner:
                self.players.remove(player)
                self.players.insert(0, player)
                if has_2_clubs:
                    print(player, " has 2 of clubs and will start the game")
                if is_prev_winner:
                    print(player, "won the last round and will lead")
                break

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

    def check_trick_winner(self, trick: list[tuple[Player, Card]]):
        [winning_player, winning_card] = trick[0]
        lead_suit = winning_card.suit
        for player, card in self.trick:
            if card.suit == lead_suit and card.value > winning_card.value:
                winning_card = card
                winning_player = player

        print(
            f"{'You' if winning_player.id == 1 else winning_player.name} won this hand"
        )
        winning_player.score += 1
        return winning_player

    def print_scores(self):
        print("\n" + "Scores on the doors...")
        for player in self.players:

            print(player.score, "-", player.name)
        print("\n")

    def check_game_over(self):
        if len(self.player1.hand) == 0:
            self.game_over = True

            print(
                """------------
Game Over
------------"""
            )
            winners = self.check_winner()
            if len(winners) == 1:
                print("THE WINNER IS .....")
                sleep(5)
                print(winners[0].name.upper())
            else:
                names = [winner.name.upper() for winner in winners]
                print("THE WINNERS ARE .....")
                sleep(5)
                print(f"{', '.join(names[:-1])} and {names[-1]}")

            self.print_scores()

    def check_winner(self):
        max_score = -1
        winners: list[Player] = []
        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                winners = [player]
                continue
            if player.score == max_score:
                winners.append(player)
        return winners
