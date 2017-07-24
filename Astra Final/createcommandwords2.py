import os

def createcommandwords2():
    l=("F820","F840","F860","F880","F8A0","F8C0")
    file=open(os.getcwd()+"\\commandwords2.txt","w+")
    for word in l:
        file.write(word+"\n")
createcommandwords2()
