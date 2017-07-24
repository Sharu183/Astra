import os

def createcommandwords3():
    l=("F820","F840","F860","F880","F8A0","F8C0","F8E0","F8F0","F800","F810")
    file=open(os.getcwd()+"\\commandwords3.txt","w+")
    for word in l:
        file.write(word+"\n")
createcommandwords3()
