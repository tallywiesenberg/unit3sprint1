''''''
import random
class Product:
    
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        stealability = self.price / self.weight
        if stealability < 0.5:
            print("Not so stealable...")
        if (stealability >= 0.5) & (stealability <= 1):
            print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        explosion = self.flammability * self.weight
        if explosion < 10:
            print("...fizzle.")
        if (explosion >= 10) & (explosion < 50):
            print("...boom!")
        else:
            print("...BABOOM!!")
    
class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        # self.name = name
        # self.price = price
        # self.weight = weight

        Product.__init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999))

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        if (self.weight >= 5) & (self.weight <= 15):
            print("Hey that hurt!")
        else:
            print("OUCH!")