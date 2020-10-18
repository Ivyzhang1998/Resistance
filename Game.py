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
        cards = ["BLUE", "RED", "BLUE", "RED", "BLUE"]
        player_list = [0,1,2,3,4]
        random.shuffle(player_list)
        for i in range(0,5):
            player_index = player_list[i]
            card = cards[i]
            player = Player(card,player_index)
            self.players[player_index] = player
    """
    Do a round of mission
    @Param: index of the mission leader
    @Return: result of the mission. False = fails; True = Mission succeeds
    """
    def do_mission(self,leader):
        player = self.players[leader]
        selected_players = player.select_players(3)
        print(selected_players)
        for i in selected_players:
            p = self.players[i]
            print(p.color)
            if p.vote == False:
                return False
        return True


g = Game(5)
g.assign_cards()
print(g.do_mission(3))
