import callextract2
import datalist2
import createreport2
import os

#FUNCTION TO FIND VALUES FROM FILE

def calculate(cw):
    commandword=str(cw)
    file=open("app2repname.txt","r")
    repfile=""
    for a in file:
        repfile=str(a)
    callextract2.extractdata(repfile)
    list=datalist2.convert(commandword)
    print(list)
    createreport2.report(list,commandword)
