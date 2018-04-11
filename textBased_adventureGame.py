class Wrestler:
    """This is the beginning of a class for the humble house wrestler"""

    def __init__(self, name):
        self.name = name
        
    def add_nicknames(self, nicknames):
        self.nicknames = nicknames

    def add_birthDate(self, birthDate):
        self.birthDate = birthDate

    def add_age(self, age):
        self.age = age

    def add_billedFrom(self, billedFrom):
        self.billedFrom = billedFrom

    def add_mass(self, mass):
        self.mass = mass

    def add_height(self, height):
        self.height = height

    def add_debut(self, debut):
        self.debut = debut
        
    def add_trainedBy(self, trainedBy):
        self.trainedBy = trainedBy

    def add_finishingMoves(self, finishingMoves):
        self.finishingMoves = finishingMoves

    def add_signatureMoves(self, signatureMoves):
        self.signatureMoves = signatureMoves

    def add_entranceThemes(self, entranceThemes):
        self.entranceThemes = entranceThemes

    def add_championships(self, championships):
         self.championships = championships

    def add_accomplishments(self, accomplishments):
        self.accomplishments = accomplishments

class Face(Wrestler):
    """Face inherits from Wrestler"""

class Tweener(Wrestler):
    """Tweener inherits from Wrestler"""

class Heel(Wrestler):
    """Heel inherits from Wrestler"""


b = Face("Bayley")

b.add_nicknames("The Huggable One")

b.add_birthDate("June 15, 1989")

b.add_age(28)

b.add_billedFrom("San Jose, California")

b.add_mass(119)

b.add_height(5)

b.add_debut("September 19, 2008")

b.add_trainedBy("Jason Styles")

b.add_finishingMoves("Bayley to Belly")

b.add_signatureMoves("Bayleycanrana")

b.add_entranceThemes("Turn It Up")

b.add_championships("WWE Raw Womens Championship and WWE NXT Womens Championship")

b.add_accomplishments("Match of the Year and Female Competitor of the Year")



m = Face("Mustafa Ali")

m.add_nicknames("Prince Ali")

m.add_birthDate("March 28, 1986 ")

m.add_age(32)

m.add_billedFrom("Chicago, Illinois")

m.add_mass(182)

m.add_height(5)

m.add_debut("February 2, 2003")

m.add_trainedBy("NXT")

m.add_finishingMoves("045")

m.add_signatureMoves("Double Jump Moonsault Side Slam")

m.add_entranceThemes("Go Hard")

m.add_championships("No Championships")

m.add_accomplishments("Has a Champiosnhip Match at Wrestlmania")



k = Tweener("Asuka")

k.add_nicknames("The Empress of Tomorrow")

k.add_birthDate("September 26, 1981 ")

k.add_age(36)

k.add_billedFrom("Osaka, Japan")

k.add_mass(137)

k.add_height(5)

k.add_debut("June 16, 2004")

k.add_trainedBy("Yuki Ishikawa")

k.add_finishingMoves("Asuka Lock")

k.add_signatureMoves("Hip Attack")

k.add_entranceThemes("The Future")

k.add_championships("WWE NXT Womens Championship")

k.add_accomplishments("Royal Rumble Winner, Mixed Match Challenge Winner, and Best Competitor of the Year")




h = Tweener("Hideo Itami")

h.add_nicknames("The International Sensation")

h.add_birthDate("March 12, 1981")

h.add_age(37)

h.add_billedFrom("Tokyo, Japan")

h.add_mass(182)

h.add_height(5)

h.add_debut("May 24, 2000")

h.add_trainedBy("Kenta Kobashi and Yoshihiro Takayama")

h.add_finishingMoves("Go To Sleep")

h.add_signatureMoves("Falcon Arrow")

h.add_entranceThemes("Time Has Come")

h.add_championships("No Championships")

h.add_accomplishments("Won the Andre the Giant Memorial Battle Memorial Qualifying Tournament")




t = Heel("Tamina Snuka")

t.add_nicknames("The Bodyguard")

t.add_birthDate("January 10, 1978")

t.add_age(40)

t.add_billedFrom("The Pacific Islands")

t.add_mass(150)

t.add_height(5)

t.add_debut("September 26, 2009")

t.add_trainedBy("Wild Samoan Training Center and FCW")

t.add_finishingMoves("Superfly Splash")

t.add_signatureMoves("Somoan Drop")

t.add_entranceThemes("What You Think")

t.add_championships("No Championships")

t.add_accomplishments("Ranked No. 19 of the top 50 female wrestlers in the PWI Female 50 in 2012")




a = Heel("Ariya Daivari")

a.add_nicknames("The Persian Lion")

a.add_birthDate("April 11, 1989")

a.add_age(28)

a.add_billedFrom("Minneapolis, Minnesota By way of Tehran, Iran")

a.add_mass(190)

a.add_height(5)

a.add_debut("September 26, 2006")

a.add_trainedBy("Arik Cannon, Ken Anderson, Shawn Daivari, and Shelton Benjamin")

a.add_finishingMoves("Persian Lion Splash")

a.add_signatureMoves("Camel Clutch")

a.add_entranceThemes("Magic Carpet Ride")

a.add_championships("No Championships")

a.add_accomplishments("Ranked #201 of the top 500 singles wrestlers in the PWI 500 in 2017")



print(b.name)
print(b.nicknames)
print(b.birthDate)
print(b.age)
print(b.billedFrom)
print(b.mass)
print(b.height)
print(b.debut)
print(b.trainedBy)
print(b.finishingMoves)
print(b.signatureMoves)
print(b.entranceThemes)
print(b.championships)
print(b.accomplishments)

print("\n\n")

print(m.name)
print(m.nicknames)
print(m.birthDate)
print(m.age)
print(m.billedFrom)
print(m.mass)
print(m.height)
print(m.debut)
print(m.trainedBy)
print(m.finishingMoves)
print(m.signatureMoves)
print(m.entranceThemes)
print(m.championships)
print(m.accomplishments)

print("\n\n")

print(k.name)
print(k.nicknames)
print(k.birthDate)
print(k.age)
print(k.billedFrom)
print(k.mass)
print(k.height)
print(k.debut)
print(k.trainedBy)
print(k.finishingMoves)
print(k.signatureMoves)
print(k.entranceThemes)
print(k.championships)
print(k.accomplishments)

print("\n\n")

print(h.name)
print(h.nicknames)
print(h.birthDate)
print(h.age)
print(h.billedFrom)
print(h.mass)
print(h.height)
print(h.debut)
print(h.trainedBy)
print(h.finishingMoves)
print(h.signatureMoves)
print(h.entranceThemes)
print(h.championships)
print(h.accomplishments)


print("\n\n")

print(t.name)
print(t.nicknames)
print(t.birthDate)
print(t.age)
print(t.billedFrom)
print(t.mass)
print(t.height)
print(t.debut)
print(t.trainedBy)
print(t.finishingMoves)
print(t.signatureMoves)
print(t.entranceThemes)
print(t.championships)
print(t.accomplishments)

print("\n\n")

print(a.name)
print(a.nicknames)
print(a.birthDate)
print(a.age)
print(a.billedFrom)
print(a.mass)
print(a.height)
print(a.debut)
print(a.trainedBy)
print(a.finishingMoves)
print(a.signatureMoves)
print(a.entranceThemes)
print(a.championships)
print(a.accomplishments)


