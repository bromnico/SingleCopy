import os, json
from shutil import disk_usage, copy

mypath = "/home/brent/Desktop"
stuffStats = disk_usage(mypath)

print(stuffStats)

fileSrc = "/home/brent/Desktop/SingleFileTest/messy/test.txt"
dirDest = "/home/brent/Desktop/SingleFileTest/cleanup"

path = os.path.split(fileSrc)
name, ext = os.path.splitext(path[1])

print("dirDest ", dirDest)
print("Source Path:", path[0])
print("Source File:", path[1])
print("name: ", name)
print("ext: ", ext)

fileDest = os.path.join(dirDest, ext)
print("My directory: ", fileDest)

# Output to File
data = [{
    'source': fileSrc,
    'destination': dirDest,
    'extension': ext
},
    {
        'source': "My Source",
        'destination': "My Destination",
        'extension': "My Extension"
    }]

with open(dirDest + "/data.txt", "w") as outfile:
    json.dump(data, outfile)

if not (os.path.exists(fileDest)):
    copy(fileSrc, fileDest)
    print("file copied")
else:
    print("skipped file", fileDest)
