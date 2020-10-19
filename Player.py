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
        if self.color == "RED":
           j = random.randint(0, 1)
           return j == 0

        return True

    #randomly select a subset of players with size k. Must select itself
    def select_players(self, k):
        player_list = [1,2,3,4,5]
        player_list.remove(self.index + 1)
        result = random.sample(player_list,k-1)
        result.append(self.index + 1)
        return result


#p = Player("RED", 2)
