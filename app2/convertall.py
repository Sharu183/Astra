
def hextodec(i):
    dec=int(str(i),16) #i is of str type
    #file.write(str(dec)+"\t")
    return dec
def hextobin(i):
    dec = int(str(i), 16)  # i is of str type
    #file.write(bin(dec) + "\t")
    return bin(dec)
def hextomps(i):
    dec = int(str(i), 16)  # i is of str type
    mps=(dec*5)/18
    #file.write(mps,+"\t")
    return mps
def hextokmph(i):
    dec = int(str(i), 16)  # i is of str type
    kmph=(dec*18)/5
    #file.write(kmph,+"\t")
    return kmph
def hextooctal(i):
    dec = int(str(i), 16)  # i is of str type
    return oct(dec)
