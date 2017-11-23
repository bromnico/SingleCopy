import os
from shutil import disk_usage, copy

mypath = "/home/pi"
stuffStats = disk_usage(mypath)

print(stuffStats)

fileSrc = "/home/pi/SingleFileTest/messy/test.txt"
dirDest = "/home/pi/SingleFileTest/cleanup"

fileparts = os.path.split(fileSrc)

print("dirDest ", dirDest)
print(fileparts[1])
fileDest = os.path.join(dirDest, fileparts[1])
print("My directory: ", fileDest)

if not (os.path.exists(fileDest)):
    copy(fileSrc, fileDest)
    print("file copied")
else:
    print("skipped file", fileDest)
