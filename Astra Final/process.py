import callextract
import datalist
import createreport
import os

#FUNCTION TO FIND VALUES FROM FILE

def calculate(cw):
    commandword=str(cw)
    file=open("app1repname.txt","r")
    repfile=""
    for a in file:
        repfile=str(a)
    callextract.extractdata(repfile)
    list=datalist.convert(commandword)
    print(list)
    createreport.report(list,commandword)
