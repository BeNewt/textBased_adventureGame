class Wrestler:
    """This is the beginning of a class for the humble house wrestler"""

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

   
print("Hello")

wrestlers = ['Bayley', 'Mustafa', 'Asuka', 'Hideo', 'Tamina', 'Ariya']

print(wrestlers)

wrestler_name = input("Pick a Wrestler: ")

mass = {'Bayley': 119, 'Mustafa': 182, 'Asuka': 137, 'Hideo': 182, 'Tamina': 150, 'Ariya': 190}
sig_moves = {'Bayley': "Bayleycanrana", 'Mustafa': "Double Jump Moonsault Side Slam" , 'Asuka': "Hip Attack" , 'Hideo': "Falcon Arrow", 'Tamina': "Somoan Drop", 'Ariya': "Camel Clutch"}
fin_moves = {'Bayley': "Bayley to Belly", 'Mustafa': "054" , 'Asuka': "Asuka Lock", 'Hideo': "Go To Sleep", 'Tamina': "Superfly Splash", 'Ariya': "Persian Lion Splash"}

if wrestler_name in wrestlers:
    player = Wrestler(wrestler_name, mass[wrestler_name])

run = True

while run:
    ans = input("\n say something: ")
    print("your answer was: " + ans)

    if ans == 'quit':
        run = False


print("Goodbye!")









    

   
