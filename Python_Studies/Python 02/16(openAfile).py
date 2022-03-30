from tkinter import * 
from tkinter import filedialog

def OpenFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\hentg\\AppData\\Local\\Programs\\Microsoft VS Code\\All Python\\Python 02",
                                         title="Open File",
                                         filetypes=(("Text Files", "*.txt"), 
                                         ("All Files", "*.*")))
    fileopen = open(filepath,"r")
    print(fileopen.read())
    fileopen.close()


window = Tk()


button = Button(text="Open", command=OpenFile)
button.pack()


window.mainloop()