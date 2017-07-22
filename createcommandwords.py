import os

def createcommandwords():
    l=("F820","F840","F860","F880","F8A0","F8C0","3C20","4420","4C20","5420","38E5","40E5","48E5","50E5","3C40","4440","4C40","5440","3C65","4465","4C65","5465","5204")
    file=open(os.getcwd()+"\\commandwords.txt","w+")
    for word in l:
        file.write(word+"\n")
createcommandwords()
