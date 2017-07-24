# PROGRAM TO CALL EXTRACT ON EACH COMMANDWORD PRESENT IN COMMANDWORDS.TXT


import extract3
import os
import createcommandwords3

def extractdata(repfile):
    createcommandwords3.createcommandwords3()
    file = open("commandwords3.txt", "r")
    lines = file.read()
    commandword = ""
    if not os.path.exists(os.getcwd()+"\\data3"):
        os.mkdir(os.getcwd()+"\\data3")
    for line in lines:
        if '\n' not in line:
            commandword += line
        if '\n' in line:
            extract3.extract3(str(commandword), str(repfile))
            # print(commandword)
            commandword = ""
