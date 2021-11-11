from Functions import *
from time import *
import random
team = input('Write Team name')
class athlete:
    team_name = team
    levels = 50
    amount = 500
    def __init__(self, name):
        self.name = name
        self.stamina = 50
        self.pace = 50
        self.striking = 50
        self.defending = 50
        self.accuracy = 50
        self.accuracy_cost = 50
        self.defending_cost = 50
        self.striking_cost = 50
        self.pace_cost = 50
        self.stamina_cost = 50

    def accuracy_boost(self, num_of_levels):
        cd = 5 * num_of_levels
        self.accuracy += cd
        self.accuracy_cost *= 1.85

    def defending_boost(self, num_of_levels):
        cd = 5 * num_of_levels
        self.defending += cd
        self.defending_cost *= 1.85

    def striking_boost(self, num_of_levels):
        cd = 5 * num_of_levels
        self.striking += cd
        self.striking_cost *= 1.85

    def pace_boost(self, num_of_levels):
        cd = 5 * num_of_levels
        self.pace += cd
        self.pace_cost *= 1.85

    def stamina_boost(self, num_of_levels):
        cd = 5 * num_of_levels
        self.stamina += cd
        self.stamina_cost *= 1.85

player_lst = []
options_lst = ['Match', 'Result', 'Edit', 'settings']
print('welcome to Soccer Unreal')
attempts = 7
while attempts:
    attempts -= 1
    name = input("Write player name: ")
    c = name
    c = athlete(name)
    player_lst.append(c)

for i in options_lst:
    sleep(1)
    print(i)
while True:
    what_to_do = input('select option: ').lower()
    if what_to_do == 'match':
        match(team)
    elif what_to_do == 'edit':
        edit(athlete, player_lst)
    elif what_to_do == 'result':
        result()


