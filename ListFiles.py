from os import listdir
from os.path import isfile, join


def listFiles(items):
    for item in items:
        print(item)


mypath = '/home/brent/Downloads'
onlyFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
num = len(onlyFiles)
print('Number of Files ' + str(num))
listFiles(onlyFiles)
print(onlyFiles)
