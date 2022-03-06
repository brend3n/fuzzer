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
       2.  Run program  {./jpgnmp [jpg] [bmp]}

    """
    argc = len(sys.argv)
    print(f"num args: {argc}")
    exec_str = f'./jpgbmp {sys.argv[1]} {sys.argv[2]}'
    print(exec_str)
    exec(exec_str)


if __name__ == "__main__":
    run()
