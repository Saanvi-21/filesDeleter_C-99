import os
import shutil
import time
import math

path = "./test"
files = os.walk(path)
limit = 2592000000000
for root, dirs, files in os.walk(path) :
    for name in files :
        path=os.path.join(root, name)
        fileTime = round(os.stat(path).st_ctime)
        if fileTime >= limit :
            os.remove(path)

    for name in dirs :
        path = os.path.join(root, name)
        fileTime = round(os.stat(path).st_ctime)
        if fileTime >= limit :
            os.remove(path)