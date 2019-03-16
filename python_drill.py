import os

path = '/Users/mac/Desktop/Python_drill'
dirs = os.listdir(path)


for file in dirs:
    if '.txt' in file:
        fPath = os.path.join(path,file)
        print(fPath,os.path.getmtime(fPath))









