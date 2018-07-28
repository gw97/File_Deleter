#will delete any file containing the substring specified in the current working directory of the program
import os
def delcontains():
    a = input('File contains:')
    dir_name = os.getcwd()
    test = os.listdir(dir_name)
    for i in test:
        if i.find(a) != -1:
            os.remove(os.path.join(dir_name, i))


