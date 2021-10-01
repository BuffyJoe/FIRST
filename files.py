from time import *
import random
class athlete:
    team = 'Ekene Fc'
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
options_lst = ['Match', 'Live', 'Edit', 'settings']
print('welcome to Soccer Unreal')
attempts = 2
while attempts:
    attempts -= 1
    name = input("Write player name: ")
    c = name
    c = athlete(name)
    player_lst.append(c)
amount = 500
alloted_levels = 5
def match():
    name = 'MUFC'
    name2 = 'LIVFC'
    global alloted_levels
    if random.randint(0,5) > random.randint(0,5):
        alloted_levels += 5
        print(alloted_levels)
    else:
        print('match lost')

def edit():
    which_player = input("Which Player to Edit: ")
    which_player2 = athlete(which_player)
    global alloted_levels
    global amount
    for c in player_lst:
        if c.name == which_player2.name:
            edit_options = ['Stamina', 'Pace', 'Striking', 'Defending', 'Accuracy']
            print(*edit_options)
            what_to_edit = input("What to edit: ").lower()
            if what_to_edit == 'accuracy':
                num_of_levels = int(input("how many levels: "))
                if num_of_levels < alloted_levels:
                    if amount >= c.accuracy_cost:
                        alloted_levels -= num_of_levels
                        amount -= c.accuracy_cost
                        c.accuracy_boost(num_of_levels)
                    else:
                        print("You cant afford this")
                    print(c.accuracy, amount)
                else:
                    print('Play more matches to earn more levels')
            elif what_to_edit == 'stamina':
                num_of_levels = int(input("how many levels: "))
                if num_of_levels < alloted_levels:
                    if amount >= c.stamina_cost:
                        alloted_levels -= num_of_levels
                        amount -= c.stamina_cost
                        c.stamina_boost(num_of_levels)
                    else:
                        print("You dont have enough Money for this")
                    print(f'your current stamina is {c.stamina}')
                else:
                    print('Win more maches to earn more levels')
            elif what_to_edit == 'pace':
                num_of_levels = int(input("how many levels: "))
                if num_of_levels < alloted_levels:
                    if amount >= c.pace_cost:
                        alloted_levels -= num_of_levels
                        amount -= c.pace_cost
                        c.pace_boost(num_of_levels)
                    else:
                        print('You dont have enough funds')
                else:
                    print("Play more matches to earn more levels")
            elif what_to_edit == 'striking':
                num_of_levels = int(input("how many levels: "))
                if num_of_levels < alloted_levels:
                    if amount >= c.striking_cost:
                        alloted_levels -= num_of_levels
                        amount -= c.striking_cost
                        c.striking_boost(num_of_levels)
                    else:
                        print('You dont have enough funds')
                else:
                    print("Play more matches to earn more levels")
            elif what_to_edit == 'defending':
                num_of_levels = int(input("how many levels: "))
                if num_of_levels < alloted_levels:
                    if amount >= c.defending_cost:
                        alloted_levels -= num_of_levels
                        amount -= c.defending_cost
                        c.defending_boost(num_of_levels)
                    else:
                        print('You dont have enough funds')
                else:
                    print("Play more matches to earn more levels")

            else:
                print("Cannont find such player")

for i in options_lst:
    sleep(1)
    print(i)
while True:
    what_to_do = input('select option: ').lower()
    if what_to_do == 'match':
        match()
    if what_to_do == 'edit':
        edit()