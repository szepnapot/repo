import random


class Combat:
    dodge_l = 6
    attack_l = 6
    '''
    def __init__(self):
        self.dodge_l = 6
        self.attack_l = 6
    '''
    def dodge(self):
        roll = random.randint(1, self.dodge_l)
        return roll > 4

    def attack(self):
        roll = random.randint(1, self.attack_l)
        return roll > 4