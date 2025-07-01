from classes import *
from random import *
import math

POPULATION_SIZE = 100

def one_point_crossover(first, second):
    index = randrange(0, min(len(first.array), len(second.array)))
    first_child = Chromosome(first.array[:index] + second.array[index:])
    second_child = Chromosome(second.array[:index] + first.array[index:])
    return first_child, second_child


def two_point_crossover(first, second):
    if len(first.array) <= 1 or len(second.array) <= 1:
        return first, second

    first_index = randrange(0, min(len(first.array), len(second.array)))
    second_index = randrange(0, min(len(first.array), len(second.array)))
    while first_index == second_index:
        second_index = randrange(0, min(len(first.array), len(second.array)))
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
    for gene in chromosome.array:
        if excess == gene.count:
            chromosome.array.remove(gene)
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


def mutation(chromosome, stock_width, stock_height):
    ''''
    Function chooses 2 genes in one chromosome. Then swaps random chosen piece from them.
    Reorder the pieces in gene

    :param chromosome: chromosome to mutate
    :return: mutated chromosome
    '''

    # this is best possible scenario, no mutation needed
    if len(chromosome.array) <= 1:
        return

    list_pairs = []
    # try to pick 2 genes with smalles area occupied
    for i in range(len(chromosome.array)):
        area = 0
        g = chromosome.array[i]
        for p in g.pieces:
            area += p[3].width * p[3].height

        list_pairs.append((area, i))

    # sorting list
    list_pairs.sort(key=lambda x: x[0])
    # rounding to higher
    ende = math.ceil(len(chromosome.array)/2)

    if len(chromosome.array) <= 3:
        ende = len(chromosome.array)

    # Picking 2 genes for mutation
    gene_id2 = gene_id1 = list_pairs[randint(0, ende - 1)][1]
    while gene_id1 == gene_id2:
        gene_id2 = list_pairs[randint(0, ende - 1)][1]

    g1 = chromosome.array[gene_id1]
    g2 = chromosome.array[gene_id2]

    pieces_from_2_genes = []
    for tuple in g1.pieces:
        pieces_from_2_genes.append(tuple[3])

    for tuple in g2.pieces:
        pieces_from_2_genes.append(tuple[3])

    shuffled_pieces = pieces_from_2_genes[:]  # Create a shallow copy
    shuffle(shuffled_pieces)

    genes = []
    tuple_list = []
    board = [[False for _ in range(stock_width)] for _ in range(stock_height)]

    for piece in shuffled_pieces:
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
            # convert dimension if piece was initaly rotated
            width = piece.height if rotation else piece.width
            height = piece.width if rotation else piece.height

            # piece must be rotated, cant fit in inital dimension
            if width > stock_width or height > stock_height:
                rotation = 1 - rotation
                #print("rotiram jer moram")

        tuple_list.append((x, y, rotation, piece))

        width = piece.height if rotation else piece.width
        height = piece.width if rotation else piece.height
        place_piece_on_position(board, r, c, width, height)

    genes.append(Gene(tuple_list))
    # cant create 2 genes from shuffled pieces, nothing happens
    if len(genes) > 2:
        return
    # from 2 genes, made 2 new genes
    elif len(genes) == 2:
        chromosome.array[gene_id1] = genes[0]
        chromosome.array[gene_id2] = genes[1]
    # from 2 genes, one is made
    else:
        chromosome.array[gene_id1] = genes[0]
        # deleting unnecesery gene
        del(chromosome.array[gene_id2])


def roulette_selection(population, elite, deathcount):
    rated = []
    for p in population:
        rated.append([p, len(p.array)])

    rated = sorted(rated, key=lambda rated: rated[1])
    # Prvih 20 najbolje sortiranih čuvamo za sledeću rundu
    for_removal = rated[elite:]
    for p in for_removal:
        # Dodajemo nasumičnost u rangiranje populacije
        p[1] *= random()

    for_removal = sorted(for_removal, key=lambda r: r[1])
    for i in range(deathcount):
        population.remove(for_removal[-(i+1)][0])


def tournament_selection(population, elite, lifecount, tour_size):
    rated = []
    for p in population:
        rated.append((p, len(p.array)))
    rated = sorted(rated, key=lambda rated: rated[1])
    # Prvih elite najbolje sortiranih čuvamo za sledeću rundu
    fittest = []
    for i in range(elite):
        fittest.append(rated[i][0])
    for_removal = rated[elite:]
    for i in range(lifecount - elite):
        chosen = set()
        tour_index = randrange(0, len(for_removal))
        best = for_removal[tour_index]
        chosen.add(tour_index)
        for j in range(tour_size - 1):
            while tour_index in chosen:
                tour_index = randrange(0, len(for_removal))
            current = for_removal[tour_index]
            if current[1] > best[1]:
                best = current
        for_removal.remove(best)
        fittest.append(best[0])
    return fittest


def ga(population, constraints, stock_width, stock_height):
    fittest = tournament_selection(population, 20, int(POPULATION_SIZE / 2), 3)
    #print("Fittest: ", len(fittest))
    offspring = []
    for i in range(math.floor(POPULATION_SIZE / 2)):
        first_index = randrange(0, len(fittest))
        second_index = randrange(0, len(fittest))
        while first_index == second_index:
            second_index = randrange(0, len(fittest))

        if random() > 0.5:
            ttuple = two_point_crossover(fittest[first_index], fittest[second_index])
            offspring.append(ttuple[0])
            offspring.append(ttuple[1])
        else:
            ttuple = one_point_crossover(fittest[first_index], fittest[second_index])
            offspring.append(ttuple[0])
            offspring.append(ttuple[1])

    deathcount = 0

    for child in offspring:
        if not check_chromosomes(constraints, child):
            offspring.remove(child)
            deathcount += 1


    population = population + offspring
    for i in range(50):
       mutation(population[randrange(0, len(population))], stock_width, stock_height)
    roulette_selection(population, 20, POPULATION_SIZE - deathcount)


def place_piece_on_position(board, r, c, width, height):
    #print("Placing : ", width, " ", height, " on position ", r, ", ", c)
    for i in range(height):
        for j in range(width):
            board[r + i][c + j] = True


def can_place_on_position(board, r, c, width, height):
    for i in range(height):
        for j in range(width):
            if r + i >= len(board) or c + j >= len(board[0]) or board[r + i][c + j]:
                return False
    return True


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

            # convert dimension if piece was initaly rotated
            width = piece.height if rotation else piece.width
            height = piece.width if rotation else piece.height

            # piece must be rotated, cant fit in inital dimension
            if width > stock_width or height > stock_height:
                rotation = 1-rotation
                #print("rotiram jer moram")

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
