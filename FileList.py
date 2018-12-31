##!/usr/bin/python3

from PIL import Image
from PIL import ExifTags
import datetime
import os
import platform
import hashlib
import pathlib

messyDirectory = "/home/pi/Desktop/SingleFileTest/messy"
cleanDirectory = "/home/pi/Desktop/SingleFileTest/cleanup"


def get_alt_date(path_to_file):
    if platform.system() == "Windows":
        stat = os.path.getctime(path_to_file)
    else:
        stat = os.path.getmtime(path_to_file)
    alt_date = datetime.datetime.fromtimestamp(stat)
    print(">> Alternate date: ",alt_date)
    return alt_date

def get_md5_hash(file):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()
        
def process_file(root,file):
    print("Processing file: ", file)

def process_photo(root,file):
    original_file = os.path.join(root,file)
    try:
        img = Image.open(original_file)
        img.exif_info = {
            ExifTags.TAGS[x]: y
            for x, y in img._getexif().items()
            if x in ExifTags.TAGS
        }
        date_original = img.exif_info["DateTimeOriginal"]
        date_time_object = datetime.datetime.strptime(date_original, '%Y:%m:%d %H:%M:%S')
        #date_information(date_time_object)
        year = str(date_time_object.year)
        month = str(date_time_object.month)
        day = str(date_time_object.day)
        hour = str(date_time_object.hour)
        minute = str(date_time_object.minute)
        second = str(date_time_object.second)
        date_prefix = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second + "_"
        
        print(">> New File Name: ", date_prefix)
        path_to_file = os.path.join(cleanDirectory,"photo",year,month,day,date_prefix+file)
        print(">> Path to File: ",path_to_file)
        pathlib.Path(os.path.join(cleanDirectory,"photo",year,month,day)).mkdir(parents=True, exist_ok=True)
        #os.mkdir(os.path.join(cleanDirectory,"photo",year,month,day))
        os.rename(original_file,path_to_file)
    except AttributeError:
        print("Error reading EXIF ATTRIBUTE info for: ", original_file)
    except KeyError:
        print("Error reading EXIF KEY info for: ", original_file)
    except ValueError:
        print("Error reading EXIF DateTime info for: ", original_file)
        print(get_alt_date(original_file))
    else:    
        print("Date Time Original: ", date_original)
    img.close()
    print("Image: ", img)
    

def date_information(dt):
    print("== Date: ", dt.date())
    print("== Time: ", dt.time())
    print("== Date-time: ", dt)
    


def main_function(root_path):
    for root, dirs, files in os.walk(root_path,topdown=False):
        for file in files:
            path_to_file = os.path.join(root, file)
            print(">>>>> Processing file: ", path_to_file)
            #print(">> File Hash: ",get_md5_hash(path_to_file))
            file_name,file_extension = os.path.splitext(file)
            if file_extension.upper() == ".JPEG" or file_extension.upper() == ".JPG":
                print(">> processing photo: ",file)
                process_photo(root, file)
            else:
                print(">> processing file: ", file)
                process_file(root, file)                
            print("====================================")  


if __name__ == '__main__':
    origin_directory = "/home/pi/Desktop/SingleFileTest/messy"
    destination_directory = "/home/pi/Desktop/SingleFileTest/cleanup"
    main_function(origin_directory)
