##!/usr/bin/python3
# from os import walk, path

from PIL import Image
from PIL import ExifTags
import datetime
import os

messyDirectory = "/home/brent/SingleFileTest/messy"
cleanDirectory = "/home/brent/SingleFileTest/cleanup"


def photo_name(file):
    img = Image.open(file)
    img.exif_info = {
        ExifTags.TAGS[x]: y
        for x, y in img._getexif().items()
        if x in ExifTags.TAGS
    }
    print(img.exif_info)
    date_raw = img.exif_info["DateTime"]
    date_original = img.exif_info["DateTimeOriginal"]
    date_digitized = img.exif_info["DateTimeDigitized"]
    print("Date Time: ", date_raw)
    print("* Date Time Original: ", date_original)
    print("Date Time Digitized: ", date_digitized)
    print(img)


f = []
for (dirpath, dirnames, filenames) in os.walk(messyDirectory):
    f.extend(filenames)
    break

print("Your files: ", filenames)
fn = (os.path.join(dirpath, filenames[0]))
fo = open(fn)
print("Name of the file: ", fo.name)
print("Closed or not: ", fo.closed)
print("Opening mode: ", fo.mode)
fo.close()

# if file is image, read the exif data from it
photo_name(fn)
