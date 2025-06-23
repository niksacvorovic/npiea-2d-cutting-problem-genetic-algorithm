from ga import *
from graphics import *

FILE_NAME = "./input/in1.txt"
def input_data():
    '''
    inputs test case from given file path FILE_NAME.
    :return:
    '''
    with open(FILE_NAME, 'r') as f:
        stock_height, stock_width = map(int, f.readline().split())
        pieces = []
        piece_counts = {}

        # Read the number of piece types
        q = int(f.readline())
        id = 0
        # Read each piece's data for q lines
        for _ in range(q):
            p_width, p_height, p_count = map(int, f.readline().split())
            pieces.append(Piece(p_width, p_height, id))
            piece_counts[id] = p_count
            id+=1
    return stock_height, stock_width, pieces, piece_counts


def main():
    seed(54)
    print("Inputing data...")
    stock_height, stock_width, pieces, piece_counts = input_data()

    print("Generating population...")
    print("stock_width:", stock_width, " stock_height:", stock_height)

    population = create_init_population(pieces, piece_counts, stock_width, stock_height)
    print("Init population done!")

    for i in range(50):
        ga(population, piece_counts)


    visualise(population[0], stock_width, stock_height)

    for i in range(50):
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
if __name__ == "__main__":
    main()