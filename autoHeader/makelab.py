import os
import platform

oper = platform.system()  # Gets OS system
if oper == 'Darwin' or oper == 'Linux':  # Checks if it's Unix based
    SLASHTYPE = r"/"
else:  # Windows lol
    SLASHTYPE = fr'\''

def main():
    numberOfActivities = int(input('How many activities?: '))
    labNumber = input('What is the lab number: ')
    if len(labNumber) == 1:  # Checks to see if the lab number is 1 digit and if it is, adds a 0 in front bc it looks nice  # bc = because
        labNumber = '0' + labNumber
    firstDir = os.path.dirname(os.path.realpath(__file__))  # Gets current url of makelab.py
    files = os.listdir(firstDir)  #  Gets all files in dir that makelab.py is in
    if 'pyfiles' not in files:  # If it can't find pyfiles folder
        os.mkdir(f'{firstDir}{SLASHTYPE}pyfiles')  # Creates pyfiles folder
    dir_path = os.path.dirname(os.path.realpath(__file__)) + f'{SLASHTYPE}pyfiles'  # Gets path to pyfiles folder
    exerciseFiles = os.listdir(dir_path)  # Checks to see if files already there
    if 'Exercise1' not in exerciseFiles:  # If there are NO files
        for num in range(1, numberOfActivities+1):
            os.mkdir(dir_path + f'{SLASHTYPE}Exercise{num}')
            w = open(dir_path + f'{SLASHTYPE}Exercise{num}{SLASHTYPE}lab{labNumber}-exercise{num}.py', 'w')
            w.write('\n')
            w.close()
    else:
        print('Files already exsist. Please delete to avoid data loss')
 
 main()
