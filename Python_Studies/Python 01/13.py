############################# write a file // w = write, r = read, a = acrescentar ( append )
#text = "Yooooooo\nThis is some text\n Have a nice one!"
#with open("endrew.txt",'w') as file:
    #file.write(text)

############################# copy a file
# copyfile() = copies contests of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata ( file's creation and modification times )
#import shutil

#shutil.copyfile("C:\\Users\\hentg\\Desktop\\test.txt", "C:\\Users\\hentg\\Desktop\\copy.txt") #src, dst

############################# move a file
import os

source = "sim"
destination = "C:\\Users\\hentg\\Desktop\\sim"

try:
    if os.path.exists(destination):
        print("There's already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+ " was not found")
