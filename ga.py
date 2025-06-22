from classes import *
from random import *

POPULATION_SIZE = 5


def one_point_crossover(first, second):
    index = randrange(0, min(len(first.pieces), len(second.pieces)))
    first_child = Chromosome(first.array[:index] + second.array[index:])
    second_child = Chromosome(second.array[:index] + first.array[index:])
    return first_child, second_child


def two_point_crossover(first, second):
    first_index = randrange(0, min(len(first.pieces), len(second.pieces)))
    second_index = randrange(0, min(len(first.pieces), len(second.pieces)))
    while first_index == second_index:
        second_index = randrange(0, min(len(first.pieces), len(second.pieces)))
    a = min(first_index, second_index)
    b = max(first_index, second_index)
    first_child = Chromosome(first.array[:a] + second.array[a:b] + first.array[b:])
    second_child = Chromosome(second.array[:a] + first.array[a:b] + second.array[b:])
    return first_child, second_child


def check_chromosomes(constraints, chromosome):
    count = {}
    for key in constraints:
        count[key] = 0
    for gene in chromosome.array:
        for key in gene.count:
            count[key] += gene.count[key]
    excess = {}
    # Ova promenljiva prati da li ostatak postoji, tj. da li su sve vrednosti rečniku ostataka 0
    noexcess = True
    for key in constraints:
        excess[key] = count[key] - constraints[key]
        noexcess = excess[key] == 0
        if excess[key] < 0:
            return False
    if noexcess:
        return True
    for gene in chromosome:
        if excess == gene.count:
            chromosome.array.pop(gene)
            return True

# mislim da moze da ima 4 "dela"
# 1) promena permutacije (bice drugaciji raspored piecova po tabli)
# 2) swap izmedju 2 gena
# 3) kao 2), ali u jednom smeru samo. Kao prebacivanje iz jednog gena u drugi
# 4) promena rotacije pieca

# ja sam mozda cak kontao da se na jednom genu, odradi x (2, 3, 10, nebitno) mutacije koje random izaberem od ovih 4.
def change_rotation(chromosome):
    pass


def swap_2_genes(chromosome):
    pass


def transfer_1_gene(chromosome):
    pass

def change_permutation(chromosome):
    pass


def mutation(chromosome):
    ''''
    Function chooses 2 genes in one chromosome. Then swaps random chosen piece from them.
    Reorder the pieces in gene

    :param chromosome: chromosome to mutate
    :return: mutated chromosome
    '''

    # this is best possible scenario, no mutation needed
    if len(chromosome.array) <= 1:
        return

    # Picking 2 genes for mutation
    gene_id2 = gene_id1 = randint(0, len(chromosome.array) - 1)
    while gene_id1 == gene_id2:
        gene_id2 = randint(0, len(chromosome.array) - 1)
    g1 = chromosome.array[gene_id1]
    g2 = chromosome.array[gene_id2]


def ga(population):
    '''
    :param population: initial population (list of chromosomes)
    :return:
    '''
    pass
    pass
    pass

def place_piece_on_position(board, r, c, width, height):
    for i in range(height):
        for j in range(width):
            board[r + i][c + j] = True


def can_place_on_position(board, r, c, width, height):
    for i in range(height):
        for j in range(width):
            if r + i >= len(board) or c + j >= len(board[0]) or board[r + i][c + j]:
                return False
    return True


def place_piece_on_board(board, piece, rot):
    '''

    :param board: inital state of board (gene)
    :param piece: piece you want to check
    :param rot: rotation (0 or 1) (0 = no rotation, 1 = 90 degree rotation)
    :return: ROW AND COLUMN where you can place piece
    '''
    # Handle rotation
    width = piece.height if rot else piece.width
    height = piece.width if rot else piece.height

    rows = len(board)
    cols = len(board[0])

    for r in range(rows - height + 1):
        for c in range(cols - width + 1):
            if can_place_on_position(board, r, c, width, height):
                return r, c

    return -1, -1


def make_chromosome_from_all_pieces(array, stock_width, stock_height):
    '''
    :param array: array of all pieces
    :param stock_width: width of stock
    :param stock_height: height of stock
    :return: chromosome
    '''
    #print("make_chromosome_from_all_pieces...")
    genes = []
    tuple_list = []
    board = [[False for _ in range(stock_width)] for _ in range(stock_height)]

    for piece in array:
        rotation = randint(0, 1)
        r, c = place_piece_on_board(board, piece, rotation)

        # transforming matrix indexing to 2-D axis indexing
        x = c
        y = r
        # reset board, creating new gene
        if x == -1 and y == -1:
            genes.append(Gene(tuple_list))
            tuple_list = []
            board = [[False for _ in range(stock_width)] for _ in range(stock_height)]
            x = y = 0
            r = c = 0

        tuple_list.append((x, y, rotation, piece))

        width = piece.height if rotation else piece.width
        height = piece.width if rotation else piece.height
        place_piece_on_position(board, r, c, width, height)


    genes.append(Gene(tuple_list))

    return Chromosome(genes)


def create_init_population(pieces, piece_counts, stock_width, stock_height):
    '''
    :param pieces: List of piece objects
    :param piece_counts: dictionary representing pair id-count
    :param stock_width: width of stock
    :param stock_height: height of stock

    :return: list of Chromosome that represent initial population
    '''
    print("Creating initial population...")
    population = []
    all_pieces = []
    for p in pieces:
        for i in range(piece_counts[p.id]):
            all_pieces.append(p)


    # Loop to create a new chromosome from given permutation of all_pieces
    for _ in range(POPULATION_SIZE):
        # Create a new chromosome by shuffling a copy of the original pieces list.
        # It's crucial to copy the list so the original list and other
        # chromosomes are not affected by the shuffle.
        shuffled_pieces = all_pieces[:]  # Create a shallow copy
        #print("Shuffled pieces: ")
        shuffle(shuffled_pieces)

        population.append(make_chromosome_from_all_pieces(shuffled_pieces, stock_width, stock_height))

    return population
