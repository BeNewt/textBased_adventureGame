class Wrestler:
    """This is the beginning of a class for the wrestler"""

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

class Moves:
    """This is the beginning of a class for moves"""

    def __init__(self, name):
        self.sig_moves = sig_moves

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


print("Hello")


wrestlers = ['Bayley', 'Mustafa', 'Asuka', 'Hideo', 'Tamina', 'Ariya']
mass = {'Bayley': 119, 'Mustafa': 182, 'Asuka': 137, 'Hideo': 182, 'Tamina': 150, 'Ariya': 190}

print(wrestlers)
print(mass)

character_name = input("Pick a Wrestler: ")
opponent_name = input("Pick an Opponent: ")


gen_moves = {'Attcks': "Dropkick", 'Throw': "DDT", 'Hold': "Sharpshooter", 'Aerial': "Moonsault"}
sig_moves = {'Bayley': "Bayleycanrana", 'Mustafa': "Double Jump Moonsault Side Slam" , 'Asuka': "Hip Attack" , 'Hideo': "Falcon Arrow", 'Tamina': "Somoan Drop", 'Ariya': "Camel Clutch"}
fin_moves = {'Bayley': "Bayley to Belly", 'Mustafa': "054" , 'Asuka': "Asuka Lock", 'Hideo': "Go To Sleep", 'Tamina': "Superfly Splash", 'Ariya': "Persian Lion Splash"}

print(gen_moves)
genWrestler_name = input("Pick a Generic Move for Your Character: ")
genOpponent_name = input("Pick a Generic Move for Your Opponent: ")


weapons = {'Thumbtacks', 'Steel Folding Chair', 'Table', 'Ladder', 'Trash Can', 'Barbed Wire Baseball Bat', 'Handcuffs', 'Kendo Sticks', 'Sledgehammer'}
print(weapons)
weaponWrestler_name = input("Pick a Weapon for Your Character: ")
weaponOpponent_name = input("Pick a Weapon for Your Opponent: ")


stipulations = {'I Quit Match', 'Ladder Match', 'Pinfall Match', 'Submission Match', 'Pinfall Anywhere Match', 'Time Limit Match'}
print(stipulations)
stip_name = input("Pick a Match Stipulation: ")


payperviews = {'Royal Rumble', 'TLC', 'Elimination Chamber', 'Money in the Bank', 'Extreme Rules', 'Survior Series', 'Summerslam', 'Wrestlemania'}
print(payperviews)
ppv_name = input("Pick a Payperview: ")


championships = {'WWE Universal Championships', 'WWE Raw Womens Championship', 'WWE Intercontinental Championship', 'WWE Cruiserweight Championship',
                 'WWE Championship', 'WWE SmackDown Womens Championship', 'WWE United States Championship'}
print(championships)
champ_name = input("Pick a Championship: ")


if character_name in wrestlers:
    player = Wrestler(wrestler_name, mass[wrestler_name])
    count = 0
    
    for x in wrestlers:
        if x == wrestler_name:
            count += 1
            print(count)
    del wrestlers[count]

if opponent_name in wrestlers:
    opponent = Wrestler(opponent_name, mass[opponent_name])
    count = 0
    
    for x in wrestlers:
        if x == opponent_name:
            count += 1
            print(count)
    del wrestlers[count]


character = Wrestler(character_name, mass[character_name])
opponent = Wrestler(opponent_name, mass[opponent_name])

run = True

while run:
    ans = input("\n say something: ")
    print("your answer was: " + ans)

    if ans == 'quit':
        run = False


print("Goodbye!")









    

   
