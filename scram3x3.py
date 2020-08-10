import random
import time

moves = (('U', 'D'), ('F', 'B'), ('R', 'L'))
directions = ('', "'", '2')
scramble_length = random.randint(17, 25)

def group_find(move):
    temp = moves[0]
    if move[0] in temp:
        return moves[0]
    else:
        temp = moves[1]
        if move[0] in temp:
            return moves[1]
        else:
            return moves[2]


def scramble():
    scramble = []
    for i in range(scramble_length):
        if i == 0:
            scramble.append(random.choice(random.choice(moves)) + random.choice(directions))
        else:
            while True:
                move = random.choice(moves)
                # print(group_find(move))
                if move != group_find(scramble[i - 1]):
                    scramble.append(random.choice(move) + random.choice(directions))
                    break

    return scramble


def index_scramble():
    index_scramble_list = []
    for thing in scramble():
        index_scramble_list.append(moves.index(group_find(thing)))

    return index_scramble_list

if __name__ == "__main__":
    print(scramble_length)
    print(scramble())
    print(index_scramble())
