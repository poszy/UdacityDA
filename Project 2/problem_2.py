#!/usr/bin/python


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return None



## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
#print (os.listdir("."))

# Let us check if this file is indeed a file!
#print (os.path.isfile("./ex.py"))

# Does the file end with .py?
#print ("./ex.py".endswith(".py"))




# 1) Scan testdir for files and directories
#   2) - If sub directories exists
#     3)  - List scan subdir for files and direcotries
#       4)  - call recursively . if they dont exists, exit back to 1)

# 1)

def scans(path):

  with os.scandir(path) as directory:
    print(path)

    for entry in directory:

      if entry.name.endswith('.c') and entry.is_file():
        filepath = os.path.join(entry)
        print(filepath)

      if entry.name.endswith('keep') and entry.is_file():
        filepath = os.path.join(entry)
        print(filepath)

      if os.path.isdir(entry):
        #print (entry.name)
        a = os.path.join(path, entry.name)
        scans(a)
        print (a)

path = "testdir"
scans(path)


#path = os.path.join(dirname, i)
