"""
Author: Jiawen Zhang
Date: 10/18/2020
"""

from Player import Player
import random
class Game:

    def __init__(self, num_player = 5):
        self.num_player = num_player
        self.players = dict()

    def assign_cards(self):
        cards = ["Blue", "Red", "Blue", "Red", "Blue"]
        player_list = [0,1,2,3,4]
        random.shuffle(player_list)
        for i in range(0,5):
            player_index = player_list[i]
            card = cards[i]
            player = Player(card,player_index)
            self.players[player_index] = player


g = Game(5)
g.assign_cards()
for index in g.players:
    player = g.players[index]
    print(player.index)
    print(player.color)
