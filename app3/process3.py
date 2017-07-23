import callextract3
import datalist3
import createreport3
import os

#FUNCTION TO FIND VALUES FROM FILE

def calculate(cw):
    commandword=str(cw)
    file=open("app3repname.txt","r")
    repfile=""
    for a in file:
        repfile=str(a)
    callextract3.extractdata(repfile)
    list=datalist3.convert(commandword)
    print(list)
    createreport3.report(list,commandword)
