from ga import *
from graphics import *

FILE_NAME = "./input/in1.txt"
stock_width = 0
stock_height = 0
pieces = []
piece_counts = {}

def input_data():
    '''
    inputs test case from given file path FILE_NAME.
    :return:
    '''
    global pieces, piece_counts, stock_width, stock_height
    with open(FILE_NAME, 'r') as f:
        stock_height, stock_width = map(int, f.readline().split())

        # Read the number of piece types
        q = int(f.readline())
        id = 0
        # Read each piece's data for q lines
        for _ in range(q):
            p_width, p_height, p_count = map(int, f.readline().split())
            pieces.append(Piece(p_width, p_height, id))
            piece_counts[id] = p_count
            id+=1


def main():
    print("Inputing data...")
    input_data()

    print("Generating population...")
    print("stock_width:", stock_width, " stock_height:", stock_height)

    population = create_init_population(pieces, piece_counts, stock_width, stock_height)
    print("Init population done!")

    for chromosome in population:
        chromosome.print()

    #for chromosome in population:
       # visualise(chromosome)

    # ga(population)

    visualise(population[0], stock_width, stock_height)

# ALGORITAM

# create init population

# ga:
#   do while (nesto)
#       crossover
#       provera dobijenih childova
#       ako moze, smanjimo broj gena u jednom chromosomu
#
#    prirodna selekcija?? bira se pola najboljih
#    nad dobijenom novom populacijom, primeniti mutaciju

# chromosomi sa najmanjom duzinom su najbolja resenja




# CLASSES

# id, x, y, rot

# gene (predstavlja jednu tablu, i id-eve piecova na njoj + rotacija)
# sadrzi kolko kojeg imam

# chromosome (predstavlja niz gena (tabli))
# piece (width, height, id)

# gui klasa (matplot lib, sta god)
# treba uraditi input (iz fajla, iz konzole + meni???)




# METHDOS

# crossoveer (prima 2 chromosoma, vraca 2 chromosoma) - urađeno                                     NIKSA
# check_chromosome (prima chromosome, provera uslove + skrati broj gena ako je moguce) - urađeno    NIKSA
# plotovanje resenja - urađeno                                                                      NIKSA
# fitness_function  MOZDA NAM NE TREBA                                                              NIKSA


# mutacija (prima chromosomm, vraca mutirani chromosome)                 VEDRAN
# input piecova + velicina table                               uradjeno  VEDRAN
# create_init_population                                                 VEDRAN
# natural_selection (80-20, nesto, treba uzimati i malo losih hromozoma) VEDRAN

if __name__ == "__main__":
    main()