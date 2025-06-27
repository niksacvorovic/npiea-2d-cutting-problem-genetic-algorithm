from ga import *
from graphics import *
import sys

FILE_NAME = "./test_cases/in3.txt"
stock_width = 0
stock_height = 0
pieces = []
piece_counts = {}

def input_data(file_name):
    '''
    inputs test case from given file path FILE_NAME.
    :return:
    '''
    global pieces, piece_counts, stock_width, stock_height
    with open(file_name, 'r') as f:
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
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as an argument.")
        print("Usage: python main.py <path_to_file>")
        return  # Exit the function


    file_name = sys.argv[1]

    print(f"Processing file: {file_name}")

    print("Inputing data...")
    input_data(file_name)

    print("Generating population...")
    print("stock_width:", stock_width, " stock_height:", stock_height)

    population = create_init_population(pieces, piece_counts, stock_width, stock_height)
    print("Init population done!")

    # ga(population)


    visualise(population[0], stock_width, stock_height)

    for i in range(1000):
        mutation(population[0], stock_width, stock_height)

    visualise(population[0], stock_width, stock_height)

'''
The GA Main Loop Begins Here:

    Sta cemo od selekcije... tournament, natural, roulette wheel??
    
a. Selection: This is where you do it. After scoring everyone in the current population, you use a selection method to pick individuals for a "mating pool." The size of this mating pool is typically the same as your population size. Fitter individuals will be selected more often.

b. Crossover (Breeding): Pick parents from the mating pool (e.g., two at a time) and apply your crossover function to them to create one or more "offspring." Repeat until you have a new population of children.

c. Mutation: Apply your mutation function to the children in the new population with a certain small probability. This introduces new genetic material.

d. Create New Generation: The collection of mutated offspring now becomes the new population for the next cycle.

e. Termination Check: Check if you have reached a termination condition (e.g., max number of generations, or fitness has stopped improving). If not, loop back to Step 2: Fitness Evaluation with your new population.
'''

# METHDOS

# crossoveer (prima 2 chromosoma, vraca 2 chromosoma) - urađeno                                     NIKSA
# check_chromosome (prima chromosome, provera uslove + skrati broj gena ako je moguce) - urađeno    NIKSA
# plotovanje resenja - urađeno                                                                      NIKSA
# fitness_function  MOZDA NAM NE TREBA                                                              NIKSA


# mutacija (prima chromosomm, vraca mutirani chromosome)       uradjeno  VEDRAN
# input piecova + velicina table                               uradjeno  VEDRAN
# create_init_population                                       uradjeno  VEDRAN
# natural_selection (80-20, nesto, treba uzimati i malo losih hromozoma) VEDRAN

if __name__ == "__main__":
    seed(54)
    main()