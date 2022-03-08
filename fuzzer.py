import sys
import os
import time
import random
import subprocess

def get_random_byte_replacement():
    return int.from_bytes(os.urandom(1), 'big')
    
def read_stdin():
    pass
# Modify the jpg pseudo-randomly to trigger bugs
def mutate(iteration, output_filename):

    # Variable to store bytes
    bytes_d = None
    
    # Read File
    with open("cross.jpg", "rb") as jpg :
        bytes_d = jpg.read()
        
    # Convert to list to modify file data
    bytes_d = list(bytes_d)
    
    '''
        #!
        this is how to modify a byte in the list
        bytes_d[0] = \xFE 
        #!
    '''
    
    # Number of modifications to make
    # num_modifications = random.randint(1,len(bytes_d)-4)
    num_modifications = 1
    
    # print(f"num_modifications: {num_modifications}")

    # Make modifications not on header and footer though (between bytes 2-len(bytes)-2)
    for i in range(num_modifications):
        
        # Random position to modify
        rand_pos = random.randint(2,len(bytes_d)-2)
        
        # Get random byte
        rand_byte_replacement = get_random_byte_replacement()
        
        # Modify byte
        bytes_d[rand_pos] = rand_byte_replacement

    # print(f"\nbytes:\n{bytes_d}\n")

    filename = f"./{output_filename}/cross_mutated_{iteration}.jpg"

    # Convert back to byte string to write to file
    bytes_d = bytes(bytes_d)

    # Writing mutated bytes to file
    with open(filename, "wb") as jpg:
        jpg.write(bytes_d)


def evaluate_results():
    print("Evaluating results")
    res_map = {"1":0,"2":0,"3":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0, }
    with open("output.txt", "r") as file_:
        for line in file_:
            if "You triggered Bug #1 !" in line:
                res_map["1"] = res_map.get("1", 0) + 1
            elif "You triggered Bug #2 !" in line:
                res_map["2"] = res_map.get("2", 0) + 1
            elif "You triggered Bug #3 !" in line:
                res_map["3"] = res_map.get("3", 0) + 1
            elif "You triggered Bug #4 !" in line:
                res_map["4"] = res_map.get("4", 0) + 1
            elif "You triggered Bug #5 !" in line:
                res_map["5"] = res_map.get("5", 0) + 1
            elif "You triggered Bug #6 !" in line:
                res_map["6"] = res_map.get("6", 0) + 1
            elif "You triggered Bug #7 !" in line:
                res_map["7"] = res_map.get("7", 0) + 1
            elif "You triggered Bug #8 !" in line:
                res_map["8"] = res_map.get("8", 0) + 1
            else:
                pass
    
    print(res_map)
    count = 0
    for item in res_map.keys():
        if res_map.get(item) == 0:
            print(f"Missing Bug #{item}.")
            count+=1
        
    if count == 0:
        print("Found all bugs!")
            
def run():

    # Check for proper input
    argc = len(sys.argv)
    # print(f"num args: {argc}")
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
    
    # time.sleep(10)
    evaluate_results()
    

if __name__ == "__main__":
    run()
