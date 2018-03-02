import os
import sys


def sorted_list_of_files() -> list:

    if(len(sys.argv) < 2):
        print("Enter directory path")
        return None

    if not os.path.isdir(sys.argv[1]):
        print("Enter DIRECTORY path")
        return None

    files = []
    inDir = os.listdir(sys.argv[1])
    for name in inDir:
        filePath = os.path.join(sys.argv[1], name)
        if(os.path.isfile(filePath)):
            files.append((name, os.stat(filePath).st_size))

    files.sort(key = lambda x: x[0])
    files.sort(key = lambda x: x[1], reverse=True)

    return files

if __name__ == '__main__':
    sortedFiles = sorted_list_of_files()
    print(sortedFiles)