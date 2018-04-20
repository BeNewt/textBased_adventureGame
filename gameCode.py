class Wrestler:
    """This is the beginning of a class for the wrestler"""

    def __init__(self, name, mass, sig_moves, fin_moves):
        self.name = name
        self.mass = mass
        self.sig_moves = sig_moves
        self.fin_moves = fin_moves

class Moves:
    """This is the beginning of a class for moves"""

    def __init__(self, name):
        self.gen_moves = gen_moves

class Weapons:
    """This is the beginning of a class for weapons"""

    def __init__(self, name):
        self.weapons = weapons

class Matches:
    """This is the beginning of a class for matches"""

    def __init__(self, name):
        self.stipulations = stipulations

class Payperviews:
    """This is the beginning of a class for the payperview"""

    def __init__(self, name):
        self.payperviews = payperviews

class Championships :
    """This is the beginning of a class for the championships"""

    def __init__(self, name):
        self.championships = championships 

def checkInput(someInput):
    print(str(len(someInput.strip())))
    return someInput

print("Hello")


wrestlers = {'Bayley', 'Mustafa', 'Asuka', 'Hideo', 'Tamina', 'Ariya'}
mass = {'Bayley': 119, 'Mustafa': 182, 'Asuka': 137, 'Hideo': 182, 'Tamina': 150, 'Ariya': 190}
sig_moves = {'Bayley': "Bayleycanrana", 'Mustafa': "Double Jump Moonsault Side Slam" , 'Asuka': "Hip Attack" , 'Hideo': "Falcon Arrow", 'Tamina': "Somoan Drop", 'Ariya': "Camel Clutch"}
fin_moves = {'Bayley': "Bayley to Belly", 'Mustafa': "054" , 'Asuka': "Asuka Lock", 'Hideo': "Go To Sleep", 'Tamina': "Superfly Splash", 'Ariya': "Persian Lion Splash"}

print("\n\n")
print(wrestlers)
print("\n\n")
print(mass)
print("\n\n")
print(sig_moves)
print("\n\n")
print(fin_moves)
print("\n\n")

user_names = ["Bayley", "Mustafa","Asuka", "Hideo", "Tamina","Ariya"]
user_response = ''
user_name = ''    

def validate(un, un_list):
    global user_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            user_name = list_item
            return False
        count += 1
    return True

while validate(user_response, user_names):
    user_response = input("What champion name would you like to use? ")

champion = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(champion.mass)


while validate(user_response, user_names):
    user_response = input("What challenger name would you like to use? ")

challenger = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(challenger.mass)


Bayleycanrana = 20
double_jump_moonsault_side_slam = 7
hip_atck = 8
falcon_arrow = 18
somoan_drop = 15
camel_clutch = 10

bayley_to_belly = 16
oh_four_five = 20
asuka_lock = 25
go_to_sleep = 13
superfly_splash = 12
persian_lion_splash = 12



# character_name = ''
# while character_name 
# character_name = input("Pick a Wrestler: ")

# opponent_name = input("Pick an Opponent: ")


gen_moves = {"Dropkick", "DDT", "Sharpshooter", "Moonsault"}
print("\n\n")
print(gen_moves)

genMove_names = ["Dropkick", "DDT","Sharpshooter", "Moonsault"]
user_response = ''
genMove_name = ''    

def validate1(un, un_list):
    global genMove_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            genMove_name = list_item
            return False
        count += 1
    return True

while validate1(user_response, gen_moves):
    user_response = input("What generic move would your champion like to use? ")


while validate1(user_response, gen_moves):
    user_response = input("What generic move would your challenger like to use? ")

print("the generic move name is: " + user_response + " -- " + genMove_name)
print(genMove_names)

dropkick = 10
DDT = 5
Sharpshooter = 20
Moonsault = 20



# genWrestler_name = input("Pick a Generic Move for Your Character: ")
# genOpponent_name = input("Pick a Generic Move for Your Opponent: ")


weapons = {'Thumbtacks', 'Steel Folding Chair', 'Table', 'Ladder', 'Trash Can', 'Barbed Wire Baseball Bat', 'Handcuffs', 'Kendo Sticks', 'Sledgehammer'}
print("\n\n")
print(weapons)

weapons_names = ["Thumbtacks", "Steel Folding Chair","Table", "Ladder", "Trash Can", "Barbed Wire Bat", "Handcuffs", "Kendo Sticks", "Sledgehammer"]
user_response = ''
weapon_name = ''    

def validate2(un, un_list):
    global weapon_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            weapon_name = list_item
            return False
        count += 1
    return True

while validate(user_response, weapons_names):
    user_response = input("What weapon would your champion like to use? ")

while validate(user_response, weapons_names):
    user_response = input("What weapon would your challenger like to use? ")

print("the weapons name is: " + user_response + " -- " + weapon_name)
print(weapons_names)

Thumbtacks = 20
steel_folding_chair = 10
Table = 10
Ladder = 25
trash_can = 10
barbed_wire_baseball_bat = 15
Handcuffs = 5
kendo_sticks = 15
sledgehammer = 15

# weaponWrestler_name = input("Pick a Weapon for Your Character: ")
# weaponOpponent_name = input("Pick a Weapon for Your Opponent: ")


stipulations = {'I Quit Match', 'Ladder Match', 'Pinfall Match', 'Submission Match', 'Pinfall Anywhere Match', 'Time Limit Match'}
print("\n\n")
print(stipulations)
# stip_name = input("Pick a Match Stipulation: ")


stipulations_names = ["I Quit Match", "Ladder Match","Pinfall Match", "Submission Match", "Pinfall Anywhere Match", "Time Limit Match"]
user_response = ''
stipulation_name = ''    

def validate3(un, un_list):
    global stipulation_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            stipulation_name = list_item
            return False
        count += 1
    return True

while validate(user_response, stipulations_names):
    user_response = input("What stipulation would you like to have? ")

print("the stipulation name is: " + user_response + " -- " + stipulation_name)
print(stipulations_names)


payperviews = {'Royal Rumble', 'TLC', 'Elimination Chamber', 'Money in the Bank', 'Extreme Rules', 'Survior Series', 'Summerslam', 'Wrestlemania'}
print("\n\n")
print(payperviews)
# ppv_name = input("Pick a Payperview: ")

payperviews_names = ["Royal Rumble", "TLC","Elimination Chamber", "Money in the Bank", "Extreme Rules", "Survior Series", "Summerslam", "Wrestlemania"]
user_response = ''
payperview_name = ''    

def validate4(un, un_list):
    global payperview_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            payperview_name = list_item
            return False
        count += 1
    return True

while validate(user_response, payperviews_names):
    user_response = input("What payperview would you like to fight at? ")

print("the payperview name is: " + user_response + " -- " + payperview_name)
print(payperviews_names)


championships = {'WWE Universal Championships', 'WWE Raw Womens Championship', 'WWE Intercontinental Championship', 'WWE Crusierweight Championship',
                 'WWE Championship', 'WWE SmackDown Womens Championship', 'WWE United States Championship'}
print("\n\n")
print(championships)
# champ_name = input("Pick a Championship: ")

championships_names = ["WWE Universal Championships", "WWE Raw Womens Championship","WWE Intercontinental Championship", "WWE Crusierweight Championship",
                     "WWE Championship", "WWE SmackDown Womens Championship", "WWE United States Championship"]
user_response = ''
championships_name = ''    

def validate5(un, un_list):
    global championships_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            championships_name = list_item
            return False
        count += 1
    return True

while validate(user_response, championships_names):
    user_response = input("What championship would you like to fight for? ")

print("the championships name is: " + user_response + " -- " + championship_name)
print(championships_names)




count = 0
for x in wrestlers:
    if x.lower() == champion_name.lower():
        if x != champion_name:
            champion_name = champion_name.title()
        champion = Wrestler(champion_name, mass[champion_name], sig_moves[champion_name], fin_moves[champion_name])
        count += 1
        # print(count)
    del wrestlers[count]
    count = 0

    for x in wrestlers:
        if x.lower() == challenger_name.lower():
            if x != challenger_name:
                challenger_name = challenger_name.title()
        challenger = Wrestler(challenger_name, mass[challenger_name])
        count += 1
        # print(count)
    del wrestlers[count]



#opponent = Wrestler(opponent_name, mass[opponent_name])

run = True

while run:
    ans = input("\n say something: ")
    print("your answer was: " + ans)

    if ans == 'quit':
        run = False


print("Goodbye!")
