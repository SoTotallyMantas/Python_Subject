

def saveToFile(data, filename):
    f = open(filename, 'w')
    f.write(data)
    f.close()

def readFromFile(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data

