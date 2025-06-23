class Piece(object):
    def __init__(self, width, height, id):
        self.id = id
        self.width = width
        self.height = height

    def print(self):
        print(self.width, self.height, self.id)


# Gene represents one "board"
class Gene(object):
    # TODO: kontam da bi bilo dobro preimnovati pieces. "pieces" asocira na pieces, a ne torke x, y, rot, piece
    def __init__(self, pieces):
        # Jedan element liste pieces je torka koja sadrži x i y koordinatu pozicije, rotaciju piecea (0, 1)  i Piece objekat
        self.pieces = pieces
        self.count = {}
        for p in pieces:
            if p[3].id not in self.count:
                self.count[p[3].id] = 1
            else:
                self.count[p[3].id] += 1
    def print(self):
        for p in self.pieces:
            print("id: ", p[3].id, " x: ", p[0], " y: ", p[1], " rot: ", p[2])


# array of gene's
class Chromosome(object):
    def __init__(self, array):
        self.array = array

    def evaluate(self):
        return len(self.array)

    def print(self):
        print("Chromosome:")
        for e in self.array:
            e.print()
            print()
        print("____________________")