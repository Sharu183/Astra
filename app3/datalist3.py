def convert(commandword):
    arr = []
    inp = open("data3/" + str(commandword) + ".txt", "r+")  # read line into array
    for line in inp.readlines():  # loop over the elemets, split by whitespace
        for i in line.split():
            arr.append(i)  # convert to integer and append to the list
    return arr
