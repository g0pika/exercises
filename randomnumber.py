import random 

class Dice:
    def roll(self):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        return r1, r2

dice = Dice()
print(dice.roll())
