import os
import datetime
import pathlib
import platform
import tarfile

oper = platform.system()  # Gets OS system
if oper == 'Darwin' or oper == 'Linux':  # Checks if it's Unix based
    SLASHTYPE = r"/"
else:  # Windows lol
    SLASHTYPE = fr'\''

dir_path = os.path.dirname(os.path.realpath(__file__))  # Gets current DIR of the .py file.

try:
    py_path = dir_path + f'{SLASHTYPE}pyfiles'
    py_files = os.listdir(py_path)
except:
    print('NO PYFILES FOLDER FOUND. CREATING ONE NOW. PLEASE PLACE YOUR PYTHON FILES IN IT.')
    os.mkdir(dir_path + f'{SLASHTYPE}pyfiles')
    py_path = dir_path + f'{SLASHTYPE}pyfiles'
    py_files = os.listdir(py_path)

all_files = os.listdir(dir_path)  # This is all files in the folder that main.py is in

def tarGivenFile(tar_filename):
    os.rename(py_path, dir_path + f'{SLASHTYPE}{tar_filename}')
    with tarfile.open(tar_filename + '.tar.gz', "w:gz") as tar:
        tar.add(dir_path + f'{SLASHTYPE}{tar_filename}', arcname=os.path.basename(dir_path + f'{SLASHTYPE}{tar_filename}'))
    os.rename(dir_path + f'{SLASHTYPE}{tar_filename}', py_path)


def checkIfConfig():
    configPresent = False
    for item in all_files:
        if item == 'config.txt':
            configPresent = True
    if configPresent == False:
        f = open(dir_path + fr'{SLASHTYPE}config.txt', 'w')
        usersname = input('NO CONFIG FILE DETECTED. CREATING NOW. Please Insert Your Name: ')
        kuid = input('NO CONFIG FILE DETECTED. CREATING NOW. Please Insert Your KUID: ')
        f.write(f'USERS_NAME: {usersname}\nUSERS_ID: {kuid}')
        f.close()

def getAllFiles(dir):
    allFiles = os.listdir(dir)
    pythonFiles = []
    for file in allFiles:
        if file[-3:-1] + file[-1] == '.py' and file != os.path.basename(__file__):  # __file__ gets this python file's name
            with open(py_path + fr'{SLASHTYPE}{file}') as text:
                lines = text.readlines()
            if lines[0][0] == "'" and lines[1][0] == 'A':
                override = input(f'{file} already has a header. Do you want to override it (y/n)?: ')
                if override.lower() == 'y':
                    pythonFiles.append(file)
            else:
                pythonFiles.append(file)
        elif '.' not in file:
            deepItems = os.listdir(dir + f'{SLASHTYPE}{file}')
            for item in deepItems:
                if item[-3:-1] + item[-1] == '.py' and item != os.path.basename(__file__):  # __file__ gets this python file's name
                    pythonFiles.append(file + f'{SLASHTYPE}{item}')
    if pythonFiles == []:
        print('NO PYTHON FILES FOUND. PLEASE PLACE THEM IN THE SAME FOLDER AS THIS PY FILE')
    return(pythonFiles)


# Function that takes the given string and adds it to the FRONT of a python file. The python file edited is the the one named FILENAME in the same DIR as the python file.
def addToPython(whatToAdd, filename):
    path = py_path + fr'{SLASHTYPE}{filename}'
    with open(path) as file:
        lines = file.readlines()
    if lines[0][0] == "'":
        for i in range(9):
            lines.pop(0)
    pureText = whatToAdd + "\n\n"
    for item in lines:
        pureText = pureText + item
    with open(path, "w") as file:
        file.write(pureText)


# Function opens config.txt and gets user's name and ID, it also takes in the Lab number and adds it to the list
def getConfig(labNumber):
    with open(dir_path + fr'{SLASHTYPE}config.txt') as file:
        config = file.readlines()
        name = config[0][12:-1]
        id = config[1][10:]
        return([name, id, labNumber])



# Takes in config settings and returns formatted header
def generateHeader(configSettings, editDate, createDate, file):
    header = f"'''\nAuthor: {configSettings[0]}\nKUID: {configSettings[1]}\nDate: {createDate}\nLab: lab{configSettings[2]}\nLast modified: {editDate}\nPurpose: {input(f'Describe {file}: ')}\n'''"
    return header


# Gets the date that the given filename in current DIR was last edited
def getEditDate(filename):
    path = py_path + fr'{SLASHTYPE}{filename}'
    epoch = pathlib.Path(path).stat().st_mtime
    converted = datetime.datetime.fromtimestamp(epoch)
    converted = converted.strftime('%m-%d-%Y')
    return(converted)


# Gets the date that the given filename in current DIR was created
def getCreateDate(filename):
    path = py_path + fr'{SLASHTYPE}{filename}'
    epoch = pathlib.Path(path).stat().st_ctime
    converted = datetime.datetime.fromtimestamp(epoch)
    converted = converted.strftime('%m-%d-%Y')
    return(converted)


def run():
    # Start of Code
    checkIfConfig()
    labNumber = input('What is the current lab number?: ')  # Gets the current lab number
    allPythonFiles = getAllFiles(py_path)
    if len(labNumber) == 1:  # Checks to see if the lab number is 1 digit and if it is, adds a 0 in front bc it looks nice
        labNumber = '0' + labNumber
    for file in allPythonFiles:
        editDate = getEditDate(file)  # Get edit date
        createDate = getCreateDate(file)  # Get create date
        addToPython(generateHeader(getConfig(labNumber), editDate, createDate, file), file)  # Feeds the labNum to the config, which feeds the config to the header generator, which feeds into the function that adds it to the file!
    wantTar = input('Do you want to tar it?: ')
    if wantTar.lower() == 'y':
        configs = getConfig(labNumber)
        tarName = f'{configs[0]}-{configs[1]}-LAB-{labNumber}'
        tarGivenFile(tarName)


run()
