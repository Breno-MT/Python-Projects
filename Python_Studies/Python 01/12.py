############################# file detection = achar o caminho de um arquivo no computador
#import os

#path = "C:\\Users\\hentg\\Desktop\\aaa"

#if os.path.exists(path):
    #print("That location exists! :) ")
    #if os.path.isfile(path):
        #print("That is a file!")
    #elif os.path.isdir(path):
        #print("That is a directory!")
#else:
    #print("That location doesn't exists! :( ")

############################# read a file
try:
    with open("C:\\Users\\hentg\\Desktop\\test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
#print(file.closed)