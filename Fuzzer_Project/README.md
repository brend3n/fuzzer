# fuzzer.py

Below are the instructions on how to run this program.


# Files

This script only uses the cross.jpg file given in the project description. You can modify the input jpg file used by changing the code. But, that is unnecessary for the purposes of this project.

## Running

To run you can use either of two commands:

    python3 fuzzer.py [X] > output.txt 2>&1
	  
, where X is the number of mutated test files to make

or

	python3 fuzzer.py [X] 2>&1

The first option allows the program to analyze the output STDOUT and STDERR properly.

However, you can run the second option to see the output on the terminal. The first option is recommended thought.
