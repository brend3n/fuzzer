import sys
import os


# Modify the jpg pseudo-randomly to trigger bugs
def mutate(filename):
    if filename[-4:] != ".jpg":
        print("JPG files only.")
        return

    # Modify contents
    with open(filename) as jpg:
        pass


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
    
    for i in range(num_iterations):
        os.system(exec_str)
    

if __name__ == "__main__":
    run()
