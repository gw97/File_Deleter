#will delete any file containing the substring specified in the current working directory of the program
import os
def delcontains(string):
    dir_name = os.getcwd()
    test = os.listdir(dir_name)
    for item in test:
        if item.find(string) != -1:
            os.remove(os.path.join(dir_name, item))

delcontains(input("Delete if file contains:"))
