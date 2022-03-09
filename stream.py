from time import sleep
import subprocess
import os

def test_if_crash(file):
    print(file)
    print(f"------------------------\nCurrent: {file}\n")
    os.system(f"./jpgbmp ./{file} del.bmp")
    print("------------------------")
    
def rename_mutations(folder_name):
    from pathlib import Path
    
    files = Path(str(folder_name)).glob('*.jpg')
    for file in files:
        test_if_crash(file)
        

rename_mutations("1646795499")