import os

def createcommandwords():
    l=("4646","4647","4648","4649","4650","4651")
    file=open(os.getcwd()+"\\commandwords.txt","w+")
    for word in l:
        file.write(word+"\n")
createcommandwords()
