import random
from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_exp = 1
    max_exp = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{} {}, HP: {}, XP: {}".format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 3
    max_exp = 2
    sound = 'time is money friend'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_exp = 2
    max_exp = 6
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_exp = 6
    max_exp = 10
    sound = 'harrrr'

