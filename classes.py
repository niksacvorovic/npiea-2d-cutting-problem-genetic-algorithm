class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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

class Gene(object):
    def __init__(self, perm_dict, array):
        self.prem_dict = perm_dict
        self.array = array