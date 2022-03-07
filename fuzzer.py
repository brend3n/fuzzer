import sys
import os
import time

# Modify the jpg pseudo-randomly to trigger bugs
def mutate(iteration, output_filename):
    
    # Read File
    with open("cross.jpg", "rb") as jpg:
        bytes_d = jpg.read()

    # Do mutations here
    print("Mutation.")
    
    print(f"\nbytes:\n{bytes_d}\n")

    filename = f"./{output_filename}/cross_mutated_{iteration}.jpg"
    # Writing mutated bytes to file
    with open(filename, "wb") as jpg:
        jpg.write(bytes_d)


def run():

    # Check for proper input
    argc = len(sys.argv)
    print(f"num args: {argc}")
    if argc < 2:
        print("Improper input: ./jpgbmp [# iterations]")
        exit(0)

    num_iterations = int(sys.argv[1])
    
    # Output file name for this run
    time_folder = int(time.time())
    os.system(f"mkdir {time_folder}")
    

    # Run all the mutations
    for i in range(num_iterations):
        curr_file = f"cross_mutated_{i}"
        print(f"Current Mutation: {curr_file}")
        mutate(i, time_folder)
        # Create command string to execute
        exec_str = f'./jpgbmp ./{time_folder}/{curr_file}.jpg ./{time_folder}/{curr_file}.bmp'
        os.system(exec_str)

if __name__ == "__main__":
    run()
