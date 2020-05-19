from random import randint

# Standard scramble: 17-25
# Include double moves (Ex: R2, F2, etc.)
# Exclude double layer moves (Ex: r, u, etc.)
# Exclude rotational moves (x, y, z, etc.)
# Exclude slice moves (M, E, S, etc.)
# U(2)/U' = excl: U(2), U', D(2), D'
# D(2)/D' = excl: U(2), U', D(2), D'
# F(2)/F' = excl: F(2), F', B(2), B'
# B(2)/B' = excl: F(2), F', B(2), B'
# R(2)/R' = excl: R(2), R', L(2), L'
# L(2)/L' = excl: R(2), R', L(2), L'
# Moves: U, U', U2, D, D', D2, F, F', F2, B, B', B2, R, R', R2, L, L', L2
# Separate moves using spaces only
# Int length later by adding length parameter
# In the future maybe allow moves like: (L, R)
scramble_length = 17
dupe_1 = ('U', "U'", 'U2', 'D', "D'", 'D2')
dupe_2 = ('F', "F'", 'F2', 'B', "B'", 'B2')
dupe_3 = ('R', "R'", 'R2', 'L', "L'", 'L2')
scramble = []
loop = range(0, scramble_length)


def scramble_3_integer():
    for _ in range(0, scramble_length):
        value = randint(0, 17)
        return value


# Generates random integer to determine directional move


def scramble_3_assignment(integer):
    if integer == 0:
        character = 'U'
        return character
    elif integer == 1:
        character = "U'"
        return character
    elif integer == 2:
        character = 'U2'
        return character
    elif integer == 3:
        character = 'D'
        return character
    elif integer == 4:
        character = "D'"
        return character
    elif integer == 5:
        character = 'D2'
        return character
    elif integer == 6:
        character = 'F'
        return character
    elif integer == 7:
        character = "F'"
        return character
    elif integer == 8:
        character = 'F2'
        return character
    elif integer == 9:
        character = 'B'
        return character
    elif integer == 10:
        character = "B'"
        return character
    elif integer == 11:
        character = 'B2'
        return character
    elif integer == 12:
        character = 'R'
        return character
    elif integer == 13:
        character = "R'"
        return character
    elif integer == 14:
        character = 'R2'
        return character
    elif integer == 15:
        character = 'L'
        return character
    elif integer == 16:
        character = "L'"
        return character
    elif integer == 17:
        character = 'L2'
        return character


# Assigns a character based on integer input
# 1
for _ in range(0, scramble_length):
    scramble.append(scramble_3_assignment(scramble_3_integer()))

# 2
print(len(scramble))

# Trying something
def check_for_dupes ():
    for x in loop:
        dupe_run = True
        if x <= scramble_length - 2:
            while (scramble[x] in dupe_1) and (scramble[x + 1] in dupe_1):
                scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
                check_for_dupes()
            while (scramble[x] in dupe_2) and (scramble[x + 1] in dupe_2):
                scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
                check_for_dupes()
            while (scramble[x] in dupe_3) and (scramble[x + 1] in dupe_3):
                scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
                check_for_dupes()

#    while scramble[x] and scramble[x + 1] in dupe_1:
#        scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
#        dupe_run = False
#    if dupe_run:
#        while scramble[x] and scramble[x + 1] in dupe_2:
#            scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
#            dupe_run = False
#    elif dupe_run:
#        while scramble[x] and scramble[x + 1] in dupe_3:
#            scramble.insert(x + 1, scramble_3_assignment(scramble_3_integer()))
#            dupe_run = False

print(scramble)
