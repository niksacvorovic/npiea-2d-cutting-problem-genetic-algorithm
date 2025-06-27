import os
import random


def generate_stock_cutting_tests(num_cases=10, folder_name="test_cases"):
    """
    Generates test case files for a 2D stock cutting problem.

    Each test file specifies the dimensions of a main sheet and a list of
    smaller rectangular pieces to be cut from it.

    Args:
        num_cases (int): The number of test case files to generate.
        folder_name (str): The name of the directory to save the files in.
    """
    # --- 1. Create the output directory if it doesn't exist ---
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Directory '{folder_name}' created or already exists.")
    except OSError as e:
        print(f"Error creating directory {folder_name}: {e}")
        return

    # --- 2. Generate each test case file ---
    for i in range(1, num_cases + 1):
        file_path = os.path.join(folder_name, f"in{i}.txt")

        try:
            with open(file_path, "w") as f:
                # --- a. Generate main paper/stock dimensions ---
                # Using a wider range for more varied problems
                paper_width = random.randint(20, 100)
                paper_height = random.randint(20, 100)
                f.write(f"{paper_width} {paper_height}\n")

                # --- b. Determine the number of unique piece types ---
                num_piece_types = random.randint(5, 15)
                f.write(f"{num_piece_types}\n")

                # --- c. Generate details for each piece type ---
                for _ in range(num_piece_types):
                    # Ensure pieces are smaller than the paper
                    # Let's make them at most 50% of the paper dimension to be realistic
                    piece_width = random.randint(1, int(paper_width * 0.5))
                    piece_height = random.randint(1, int(paper_height * 0.5))

                    # Randomly decide to keep orientation or allow rotation
                    if random.choice([True, False]):
                        # swap width and height
                        piece_width, piece_height = piece_height, piece_width

                    quantity = random.randint(1, 10)

                    f.write(f"{piece_width} {piece_height} {quantity}\n")

            print(f"Successfully generated {file_path}")

        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")


if __name__ == "__main__":
    generate_stock_cutting_tests(10)
    print("\nTest case generation complete.")
