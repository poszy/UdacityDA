#!/usr/bin/python
import os


# 1) Scan testdir for files and directories
#   2) - If sub directories exists
#     3)  - List scan subdir for files and direcotries
#       4)  - call recursively . if they dont exists, exit back to 1)

def find_files(suffix, path):

  with os.scandir(path) as directory:
    print(path)

    for entry in directory:

      if entry.name.endswith(suffix) and entry.is_file():
        filepath = os.path.join(entry)
        print(filepath)

      # This will always return .gitkeep files
      if entry.name.endswith('keep') and entry.is_file():
        filepath = os.path.join(entry)
        print(filepath)

      if os.path.isdir(entry):
        joinedPath = os.path.join(path, entry.name)
        find_files(suffix, joinedPath)
        print (joinedPath)

# Test Case 1
path = "testdir"
suffix = ".c"
find_files(suffix, path)

# Test Case 2
path = "testdir"
suffix = "."
find_files(suffix, path)


# Test Case 3
path = "testdir"
suffix = ".emacs"
find_files(suffix, path)

