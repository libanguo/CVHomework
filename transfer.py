import os
from shutil import copyfile

path = "data/cfnet-validation"
print(path)
listdir = os.listdir(path)
path1 = os.path.join('result')
path2 = os.path.join('result1')
for i in range(len(listdir)):
    path3 = path + "/" + listdir[i] + "/" + "groundtruth1.txt"
    path4 = path1 + "/" + listdir[i] + ".txt"
    copyfile(path3, path4)
    path5 = path + "/" + listdir[i] + "/" + "groundtruth.txt"
    path6 = path2 + "/" + listdir[i] + ".txt"
    copyfile(path5, path6)
