import os
import pathlib


print(os.getcwd())

p = pathlib.Path('c:/CodingStuff')

os.chdir(p)

print(os.getcwd())

#os.chdir('..')

#print(os.getcwd())

d = os.scandir('.')

for directory in d:
    print(directory.name)
    print(directory.is_dir())


def listDirectorys(path, indent):

    for directory in os.scandir(path):
        print(indent+directory.name)
        if directory.is_dir():
            listDirectorys(directory.path, indent+"\t")


listDirectorys(".", "")
