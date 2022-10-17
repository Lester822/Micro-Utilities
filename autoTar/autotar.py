import os
import platform
import tarfile

# Checks platform
oper = platform.system()  # Gets OS system
if oper == 'Darwin' or oper == 'Linux':  # Checks if it's Unix based
    SLASHTYPE = r"/"
else:  # Windows
    SLASHTYPE = fr'\''
    
dir_path = os.path.dirname(os.path.realpath(__file__))
tar_path = f'{dir_path}{SLASHTYPE}tarfolder'


def main():
    """ Main function of the program (tarring things)"""
    files = os.listdir(dir_path)  # Gets all files in the same folder as autotar.py
    if 'tarfolder' not in files:  # Checks if tarfolder is in same folder as autotar.py
        print('NO TARFOLDER FOUND. MAKING ONE')
        os.mkdir(f'{dir_path}{SLASHTYPE}tarfolder')  # Creates /tarfolder
    with tarfile.open(tar_path + '.tar.gz', "w:gz") as tar:  # Creates tar
        tar.add(dir_path, arcname=os.path.basename(dir_path + f'{SLASHTYPE}filetar'))

main()
