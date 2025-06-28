from ga import *
from graphics import *
from time import perf_counter
import sys

FILE_NAME = "./test_cases/in3.txt"
stock_width = 0
stock_height = 0
pieces = []
piece_counts = {}
testing = 0

def input_data(file_name):
    '''
    inputs test case from given file path FILE_NAME.
    :return:
    '''
    global pieces, piece_counts, stock_width, stock_height
    with open(file_name, 'r') as f:
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


def main():
    if testing:
        if len(sys.argv) < 2:
            print("Error: Please provide a file path as an argument.")
            print("Usage: python main.py <path_to_file>")
            return  # Exit the function
        file_name = sys.argv[1]
    else:
        file_name = FILE_NAME

    print(f"Processing file: {file_name}")

    print("Inputing data...")
    input_data(file_name)

    print("Generating population...")
    print("stock_width:", stock_width, " stock_height:", stock_height)

    population = create_init_population(pieces, piece_counts, stock_width, stock_height)
    print("Init population done!")

    visualise(population[0], stock_width, stock_height)

    start = perf_counter()
    iter = 0
    while perf_counter() - start < 20:
        ga(population, piece_counts, stock_width, stock_height)
        iter += 1


    visualise(population[0], stock_width, stock_height)
    print(f"Generation count: {iter}")

if __name__ == "__main__":
    seed(54)
    main()