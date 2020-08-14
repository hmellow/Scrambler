# Normals are for all puzzles where all 3 sides are the same
# 37 is Skewb
normals = {
    2: {'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'", '2')},
    3: {'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'", '2')},
    4: {'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'", '2', 'w2', 'w', "w'")},
    5: {'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'", '2', 'w2', 'w', "w'")},
    37: {'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'")}
}

# Irregulars are for puzzles with different sized sides. Use tuples as the key according to (sizeX, sizeY, sizeZ)
irregulars = {
    None
}

# Others are for other, will vary case by case
others = {
    None
}