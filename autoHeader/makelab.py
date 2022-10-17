import os
import platform

oper = platform.system()  # Gets OS system
if oper == 'Darwin' or oper == 'Linux':  # Checks if it's Unix based
    SLASHTYPE = r"/"
else:  # Windows lol
    SLASHTYPE = fr'\''

numberOfActivities = int(input('How many activities?: '))
labNumber = input('What is the lab number: ')

if len(labNumber) == 1:  # Checks to see if the lab number is 1 digit and if it is, adds a 0 in front bc it looks nice  # bc = because
    labNumber = '0' + labNumber

dir_path = os.path.dirname(os.path.realpath(__file__)) + f'{SLASHTYPE}pyfiles'
for num in range(1, numberOfActivities+1):
    os.mkdir(dir_path + f'{SLASHTYPE}Exercise{num}')
    w = open(dir_path + f'{SLASHTYPE}Exercise{num}{SLASHTYPE}lab{labNumber}-exercise{num}.py', 'w')
    w.write('\n')
    w.close()


