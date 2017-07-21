# PROGRAM TO CALL EXTRACT ON EACH COMMANDWORD PRESENT IN COMMANDWORDS.TXT


import extract
import os
import createcommandwords

def extractdata(repfile):
    createcommandwords.createcommandwords()
    file = open("commandwords.txt", "r")
    lines = file.read()
    commandword = ""
    if not os.path.exists(os.getcwd()+"\\data"):
        os.mkdir(os.getcwd()+"\\data")
    for line in lines:
        if '\n' not in line:
            commandword += line
        if '\n' in line:
            extract.extract(str(commandword), str(repfile))
            # print(commandword)
            commandword = ""
