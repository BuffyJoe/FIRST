import random
from time import *
def match(team):
    print(team)
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


def edit(athlete, player_lst):
        which_player = input("Which Player to Edit: ")
        which_player2 = athlete(which_player)
        for c in player_lst:
            if c.name == which_player2.name:
                edit_options = ['Stamina', 'Pace', 'Striking', 'Defending', 'Accuracy']
                print(*edit_options)
                what_to_edit = input("What to edit: ").lower()
                if what_to_edit == 'accuracy':
                    num_of_levels = int(input("how many levels: "))
                    if num_of_levels < athlete.levels:
                        if athlete.amount >= c.accuracy_cost:
                            athlete.levels -= num_of_levels
                            athlete.amount -= c.accuracy_cost
                            c.accuracy_boost(num_of_levels)
                        else:
                            print("You cant afford this")
                        print(c.accuracy, athlete.amount)
                    else:
                        print('Play more matches to earn more levels')
                elif what_to_edit == 'stamina':
                    num_of_levels = int(input("how many levels: "))
                    if num_of_levels < athlete.levels:
                        if athlete.amount >= c.stamina_cost:
                            athlete.levels -= num_of_levels
                            athlete.amount -= c.stamina_cost
                            c.stamina_boost(num_of_levels)
                        else:
                            print("You dont have enough Money for this")
                        print(f'your current stamina is {c.stamina}')
                    else:
                        print('Win more maches to earn more levels')
                elif what_to_edit == 'pace':
                    num_of_levels = int(input("how many levels: "))
                    if num_of_levels < athlete.levels:
                        if athlete.amount >= c.pace_cost:
                            athlete.levels -= num_of_levels
                            athlete.amount -= c.pace_cost
                            c.pace_boost(num_of_levels)
                            print(f'{c.pace} is your new pace')
                        else:
                            print('You dont have enough funds')
                    else:
                        print("Play more matches to earn more levels")
                elif what_to_edit == 'striking':
                    num_of_levels = int(input("how many levels: "))
                    if num_of_levels < athlete.levels:
                        if athlete.amount >= c.striking_cost:
                            athlete.levels -= num_of_levels
                            athlete.amount -= c.striking_cost
                            c.striking_boost(num_of_levels)
                        else:
                            print('You dont have enough funds')
                    else:
                        print("Play more matches to earn more levels")
                elif what_to_edit == 'defending':
                    num_of_levels = int(input("how many levels: "))
                    if num_of_levels < athlete.levels:
                        if athlete.amount >= c.defending_cost:
                            athlete.levels -= num_of_levels
                            athlete.amount -= c.defending_cost
                            c.defending_boost(num_of_levels)
                        else:
                            print('You dont have enough funds')
                    else:
                        print("Play more matches to earn more levels")

                else:
                    print("Cannont find such player")

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


def log_in():
    x = 1
    print('Welcome user to log-in put your details')
    while x:
        username = input('What is your username: \n').lower()
        password = input('What is your password \n password is case sensitive: \n')
        file1 = open('username', 'r')
        file2 = open('password', 'r')
        for line in file1:
            if line == username and password in file2:
                print('welcome user')
                x -= 1
            elif line != username and password not in file2:
                print('This user is not recorgnized')
                print('if you are new try signing up')
                break
            elif line == username and password not in file2:
                print("wrong password try again")
                break
            else:
                print('could not complete this action')
        file2.close()
        file1.close()

def sign_up():
    print('welcome guest to sign-up fill in the following')
    x = 1
    while x:
        username = input('What is your username: \n').lower()
        password = input('What is your password \n password is case sensitive: \n')
        file1 = open('username', 'a')
        file2 = open('password', 'a')
        file1.write(username)
        # i cant get the username and password to be entered in my text file
        # i want them entered on a new line for every new signup
        password_confirm = input('Input password again')
        if password == password_confirm:
            file2.write(password)
            print('Account created successfully')
            log_in()
            x -= 1
        else:
            print('password does not match')
sign_up()
def settings():
    setting_opt = ['LOGIN', 'LOG-OUT', 'BUY', 'SELL']
    print(setting_opt)
    what_to_do = input('Which setting to edit')
    if what_to_do == 'LOG-IN':
        log_in()