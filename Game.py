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
        self.curr_set = [] #current subset of players that are doing mission
        self.rounds_logs = dict()
        self.num_misison_players = [2, 3, 2, 3,3]
        #round number = player number
        #key: round number ; value: (selected_players, result)

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
    @Return: (leader, selected_players, result = False/True).
    False = fails; True = Mission succeeds
    """
    def do_mission(self,round_num, selected_players = None):
        if selected_players == None:
           player = self.players[round_num]
           k = self.num_misison_players[round_num]
           selected_players = player.select_players(k)
        self.curr_set = selected_players
        print(self.curr_set)
        for i in self.curr_set:
            p = self.players[i]
            if p.vote() == False:
                self.rounds_logs[round_num] = (selected_players, False)
                return
        self.rounds_logs[round_num] = (selected_players, True)

    def do_all_missions(self):
        win_count = 0
        for player_num in self.players:
            self.do_mission(player_num)
            result_tuple  = self.rounds_logs[player_num]
            result = result_tuple[1]
            if result:
                win_count += 1
        if win_count >= 3:
            return True
        return False


g = Game(5)
g.assign_cards()
count = 0
for i in range(0,100):
   if g.do_all_missions():
       count += 1
print(count)       
