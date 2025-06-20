class Piece(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height

# TODO: rename to gen
class Permutation(object):
    def __init__(self, board, rectangles):
        self.rectangles = rectangles
        self.board = board
        self.coverage = None
    def calculate_coverage(self):
        area = self.board.width * self.board.height
        covered = 0
        for rec in self.rectangles:
            covered += rec.width * rec.height
        self.coverage = covered / area

# TODO: rename to chromosome
class Gene(object):
    def __init__(self, perm_dict, array):
        self.perm_dict = perm_dict
        self.array = array