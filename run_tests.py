import os
import subprocess

# --- Configuration ---
# 1. The folder where your test cases are located.
test_case_folder = "test_cases"

# 2. The command to run your GA program.
#    Replace "./my_ga_program" with the actual command.
#    For example, it could be "python main.py" or "target/release/my_program.exe"
program_command = ["python", "main.py"]

# --- Main Execution Logic ---
# Check if the test case directory exists
if not os.path.isdir(test_case_folder):
    print(f"Error: Test case folder '{test_case_folder}' not found.")
    print("Please run the test case generator script first.")
else:
    # Get a sorted list of all test files
    try:
        # We sort the files to ensure they run in order (in1.txt, in2.txt, ...)
        test_files = sorted([f for f in os.listdir(test_case_folder) if f.startswith('in') and f.endswith('.txt')])
    except OSError as e:
        print(f"Error reading directory {test_case_folder}: {e}")
        test_files = []

    if not test_files:
        print(f"No test files found in '{test_case_folder}'.")
    else:
        print(f"Found {len(test_files)} test cases. Starting execution...")

        # Loop through each test file and run your program
        for test_file in test_files:
            file_path = os.path.join(test_case_folder, test_file)

            print(f"\n----- Running test: {file_path} -----")

            try:
                # Construct the full command with the file path as an argument
                command_to_run = program_command + [file_path]

                # Execute the command
                # capture_output=True will store stdout/stderr in the result object
                # text=True decodes them as text
                result = subprocess.run(
                    command_to_run,
                    check=True,
                    capture_output=True,
                    text=True
                )

                # Print the output from your program
                print("Output:")
                print(result.stdout)

            except FileNotFoundError:
                print(f"Error: Program '{program_command[0]}' not found.")
                print("Please make sure the 'program_command' variable is set correctly.")
                break  # Stop the script if the program doesn't exist
            except subprocess.CalledProcessError as e:
                # This block runs if your program returns a non-zero exit code (an error)
                print(f"Error running program with {file_path}.")
                print(f"Return code: {e.returncode}")
                print(f"Output (stdout):\n{e.stdout}")
                print(f"Error Output (stderr):\n{e.stderr}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        print("\n----- All tests complete -----")