# PROGRAM TO CALL EXTRACT ON EACH COMMANDWORD PRESENT IN COMMANDWORDS.TXT


import extract2
import os
import createcommandwords2

def extractdata(repfile):
    createcommandwords2.createcommandwords2()
    file = open("commandwords2.txt", "r")
    lines = file.read()
    commandword = ""
    if not os.path.exists(os.getcwd()+"\\data2"):
        os.mkdir(os.getcwd()+"\\data2")
    for line in lines:
        if '\n' not in line:
            commandword += line
        if '\n' in line:
            extract2.extract2(str(commandword), str(repfile))
            # print(commandword)
            commandword = ""
