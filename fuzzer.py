import sys
import os
import time

# Modify the jpg pseudo-randomly to trigger bugs
def mutate(iteration, output_filename):
    

    # Read File
    with open("cross.jpg", "rb") as jpg:
        bytes_d = jpg.read()

    # Do mutations here
    print("Mutation occurred.")

    filename = f"./{output_filename}/cross_mutated_{iteration}.jpg"
    # Writing mutated bytes to file
    with open(filename, "wb") as jpg:
        jpg.write(bytes_d)


def run():

    """
    Goal    execute with randomly generated mutations to break code

    Ways to break code:
        1. Integer Overflow
        2.

    8 total bugs

    
    Steps:
       1.  Mutate jpg
       2.  Run program  {./jpgbmp [number iterations] [other stuff]}

    """

    argc = len(sys.argv)
    print(f"num args: {argc}")
    if argc < 2:
        print("Improper input: ./jpgbmp [# iterations]")
        exit(0)
    num_iterations = int(sys.argv[1])

    exec_str = f'./jpgbmp {num_iterations}'
    print(exec_str)
    
    # Output file name for this run
    time_folder = int(time.time())
    os.system(f"mkdir {time_folder}")

    for i in range(num_iterations):
        print("Current Mutation: cross_mutated_{i}.jpg")
        mutate(i, time_folder)
        os.system(exec_str)
    

if __name__ == "__main__":
    run()
