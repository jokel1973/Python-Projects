import os

def writeData():
    data = '\nHello World!'
    with open('test7.txt', 'a') as f:
        f.write(data)
        f.close()

def openFile():
    with open('test7.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()  
