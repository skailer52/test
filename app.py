import os

#Get current working directory
cwd = os.getcwd()
print(cwd)

#List files and folders
ls = os.listdir()
print(ls)

def add(x,y): 
    return x + y