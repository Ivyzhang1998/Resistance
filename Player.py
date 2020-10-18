"""
Author: Jiawen Zhang
Date: 10/18/2020
"""

import random
class Player:

    def __init__(self, color, index):
        self.index = index
        self.color = color

    def vote(self):
        if self.color ==  "RED":
           j = random.randint(0, 1)
           return j == 0

        return True

    #select a subset of players with size k. Must select itself
    def select_players(self, k):
        player_list = [0,1,2,3,4]
        player_list.remove(self.index)
        result = random.sample(player_list,k-1)
        result.append(self.index)
        return result


#p = Player("RED", 2)
