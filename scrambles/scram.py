import random

components_3x3 = {
    'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 
    'directions': ('', "'", '2')
    }

class Scram():
    scramble = []

    def __init__(self, components, min, max):
        self.components = components
        self.scramble_length = random.randint(min, max)
    
    def group_find(self, move):

        for i in range(len(self.components['moves'])):
            if move[0] in self.components['moves'][i]:
                return self.components['moves'][i]

    def scram(self):
        for i in range(self.scramble_length):
            if i == 0:
                self.scramble.append(random.choice(random.choice(self.components['moves'])) + random.choice(self.components['directions']))
            else:
                while True:
                    move = random.choice(self.components['moves'])
                    if move != self.group_find(self.scramble[i - 1]):
                        self.scramble.append(random.choice(move) + random.choice((self.components['directions'])))
                        break
    
    def convert(self):
        scramble = ' '.join(self.scramble)