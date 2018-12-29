##!/usr/bin/python3

from PIL import Image
from PIL import ExifTags
import datetime
import os
import platform
import hashlib

messyDirectory = "/home/pi/Desktop/SingleFileTest/messy"
cleanDirectory = "/home/pi/Desktop/SingleFileTest/cleanup"


def creation_date(path_to_file):
    if platform.system() == "Windows":
        return os.path.getctime(path_to_file)
    else:
        stat = os.path.getctime(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            return stat.st_mtime

def get_md5_hash(file):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()
        
def process_file(file):
    print("Processing file: ", file)

def process_photo(file):
    try:
        img = Image.open(file)
        img.exif_info = {
            ExifTags.TAGS[x]: y
            for x, y in img._getexif().items()
            if x in ExifTags.TAGS
        }
        #print("===== EXIF Info: ",img.exif_info)
        date_original = img.exif_info["DateTimeOriginal"]
        date_time_object = datetime.datetime.strptime(date_original, '%Y:%m:%d %H:%M:%S')
        print("Date: ", date_time_object.date())
        print("Time: ", date_time_object.time())
        print("Date-time: ", date_time_object)
        year = str(date_time_object.year)
        month = str(date_time_object.month)
        day = str(date_time_object.day)
        hour = str(date_time_object.hour)
        minute = str(date_time_object.minute)
        second = str(date_time_object.second)
        new_file_name = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second + "_" + "orig" + ".jpg"
        print(">> New File Name: ", new_file_name)
    except AttributeError:
        print("Error reading EXIF ATTRIBUTE info for: ", file)
    except KeyError:
        print("Error reading EXIF KEY info for: ", file)
    except ValueError:
        print("Error reading EXIF DateTime info for: ", file)
    else:    
        print("Date Time Original: ", date_original)
    img.close()
    print("Image: ", img)

def main_function(root_path):
    for root, dirs, files in os.walk(root_path,topdown=False):
        for file in files:
            path_to_file = os.path.join(root, file)
            print(">>>>> Processing file: ", path_to_file)
            print(">> File Hash: ",get_md5_hash(path_to_file))
            file_name,file_extension = os.path.splitext(file)
            if file_extension.upper() == ".JPEG" or file_extension.upper() == ".JPG":
                print(">> processing photo: ",file)
                process_photo(path_to_file)
            else:
                print(">> processing file: ", file)
                process_file(path_to_file)
                
            #mills = os.path.getctime(path_to_file)
            #date = datetime.datetime.fromtimestamp(mills)
            #print(">> Created on: ",date)
            #print(">> Created on: ",creation_date(path_to_file))
            print("====================================")  


if __name__ == '__main__':
    print("We have started the main function.")
    origin_directory = "/home/pi/Desktop/SingleFileTest/messy"
    destination_directory = "/home/pi/Desktop/SingleFileTest/cleanup"
    main_function(origin_directory)
