from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile( initialdir="C:\\Users\\hentg\\Desktop",
                                     defaultextension=".txt",
                                     filetypes=[("Text File", ".txt"),("HTML File", ".html"),
                                     ("All file", ".*")])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()



window = Tk()

button = Button(text="Save", command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()