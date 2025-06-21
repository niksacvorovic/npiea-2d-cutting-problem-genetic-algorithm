class Piece(object):
    def __init__(self, id, width, height):
        self.id = id
        self.width = width
        self.height = height

# Gene represents one "board"
class Gene(object):
    def __init__(self, pieces):
        # Jedan element liste pieces je torka koja sadrži x i y koordinatu pozicije i Piece objekat
        self.pieces = pieces
        self.count = {}
        for p in pieces:
            if p[2].id not in self.count:
                self.count[p[2].id] = 1
            else:
                self.count[p[2].id] += 1

# array of gene's
class Chromosome(object):
    def __init__(self, array):
        self.array = array