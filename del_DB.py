import os, glob

def Del(filename):
    for file in glob.glob(filename):
        os.remove(file)