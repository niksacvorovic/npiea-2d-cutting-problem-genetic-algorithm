class Piece(object):
    def __init__(self, id, width, height):
        self.id = id
        self.width = width
        self.height = height

class Gene(object):
    def __init__(self, board, pieces):
        # Jedan element liste pieces je torka koja sadrži x i y koordinatu pozicije i Piece objekat
        self.pieces = pieces
        self.board = board
        self.coverage = None
        self.count = {}
        for p in pieces:
            if p[2].id not in self.count:
                self.count[p[2].id] = 1
            else:
                self.count[p[2].id] += 1
    def calculate_coverage(self):
        area = self.board.width * self.board.height
        covered = 0
        for rec in self.rectangles:
            covered += rec.width * rec.height
        self.coverage = covered / area

class Chromosome(object):
    def __init__(self, array):
        self.array = array