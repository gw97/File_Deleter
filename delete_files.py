import os

def dccwd():
    #will delete any file containing the substring specified in the current working directory of the program
    a = input('Files contain:')
    dir_name = os.getcwd()
    test = os.listdir(dir_name)
    for i in test:
        if i.find(a) != -1:
            os.remove(os.path.join(dir_name, i))



def dcswd():
    #deletes files containing a certain substring (as specified), in the directory of users choice
    dir_name = input('Specify Directory:')
    a = input('Files contain:')
    dir_name = os.getcwd()
    test = os.listdir(dir_name)
    for i in test:
        if i.find(a) != -1:
            os.remove(os.path.join(dir_name, i))