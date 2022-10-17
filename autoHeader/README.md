#autoHeader

Auto Header is a program that will automatically take python files and put a header at the top of them.
It will also ask if you would like to tar the files in the folder for easy submission.
The header wil be in this format:

'''
Author: NAME
KUID: ID
Date: DATE CREATED
Lab: LAB NUM
Last modified: DATE LAST MODIFIED
Purpose: USER GIVEN PURPOSE
'''

NAME and ID are gotten from config.txt, which will be automatically created
DATE and LAST MODIFIED are gotten from .py file data
Lab is provided during run
Purpose is provided during run

Steps to use:
1) Run the program for the first time
    * It will ask you for your name and KU ID to make the config file
    * It will also create a folder named /pyfiles
2) Put your .py files in /pyfiles folder
    * Can be within a folder in pyfiles
3) Run the program and enter details
4) Type y or n to confirm whether or not you would like it to tar the entire /pyfiles folder

IN ADDITION:

makelab.py will automatically create folders and .py files in PYFILES if you have lots of files to create.

Steps to use:
1) Run the program, if there is no pyfiles folder, it will create one.
2) Give it the lab number and the number of files you need
