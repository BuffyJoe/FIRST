from time import *
import random
team = input('Write Team name')
class athlete:
    team_name = team
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
attempts = 5
while attempts:
    attempts -= 1
    name = input("Write player name: ")
    c = name
    c = athlete(name)
    player_lst.append(c)
amount = 500
alloted_levels = 5
def match(name=team):
    print(name)
    lst_opp = []
    opponents = open('Seria A', 'r')
    for i in opponents:
        lst_opp.append(i[:-1])
    diff = ['Hard', 'Mid', "Easy"]
    diff_ch = input('Select your difficulty \n (Hard/Mid/Easy').lower()
    opp1 = random.choice(lst_opp)
    print(f'Your opponents are {opp1}, \n and difficulty is {diff_ch}')
    print(ctime(2.0))
    print('')
    if diff_ch == 'hard':
        home_score = random.randint(0,5)
        away_score = random.randint(2,5)
    elif diff_ch == 'mid':
        home_score = random.randint(0,5)
        away_score = random.randint(0,5)
    elif diff_ch == 'easy':
        home_score = random.randint(2,5)
        away_score = random.randint(0,3)
    else:
        print('Invalid Choice')
    sleep(1)
    print('Both teams start at 0:0, \nlets see how the match goes')
    sleep(5)
    if home_score > away_score:
        print('The home team cannot be stopped')
        print(f'{team} vs {opp1}, scores are\n {home_score} : {away_score}')
    elif home_score == away_score:
        print('i can see this match going either way i guess we we will just have to see')
        print(f'{team} vs {opp1}, scores are\n {home_score} : {away_score}')
    elif home_score < away_score:
        print('This is looking really bad for the home team')
        print(f'{team} vs {opp1}, scores are\n {home_score} : {away_score}')
    sleep(5)
    home_score += random.randint(0,2)
    away_score += random.randint(0,2)
    if home_score > away_score:
        print('Victory to the home team')
        print(f'full time \n {team} vs {opp1} \n {home_score} : {away_score}')
    elif home_score == away_score:
        print('like i said both teams had a chance')
        print(f'full time \n {team} vs {opp1} \n {home_score} : {away_score}')
    elif home_score < away_score:
        print('Utter Defeat, they must feel ashamed')
        print(f'full time \n {team} vs {opp1} \n {home_score} : {away_score}')

def result():
    teams = []
    fix1_team = []
    length = 0
    league = open('Seria A', 'r')
    for i in league:
        teams.append(i)
        length += 1
    length = length//2
    for i in range(length):
        fix1 = random.choice(teams)
        fix1_team.append(fix1)
        team = teams.index(fix1)
        teams.pop(team)
    for i in teams:
        for j in fix1_team:
            print(f'{i} vs {j}', end=" ")
            print(f'{random.randint(0,5)} : {random.randint(0,5)}\n')
            team_index = fix1_team.index(j)
            fix1_team.pop(team_index)
            break

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
    elif what_to_do == 'edit':
        edit()
    elif what_to_do == 'result':
        result()