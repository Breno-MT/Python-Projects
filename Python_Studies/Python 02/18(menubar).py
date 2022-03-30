from tkinter import *
from tkinter import filedialog

# ----

def OpenFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\hentg\\Desktop",
                                        title="Open File", 
                                        filetypes=(("Text Files", ".txt"), ("All Files", ".*")),
                                        )
    fileopen = open(filepath, "r")
    print(fileopen.read())
    fileopen.close()

def SaveFile():
    file = filedialog.asksaveasfile( initialdir="C:\\Users\\hentg\\Desktop",
                                     defaultextension=".txt",
                                     filetypes=(("Text File", ".txt"), ("All Files", ".*"))
                                     )

# ----

def cut():
    print("You cut some text!")

def copy():
    print("You copied some text!")

def paste():
    print("You pasted some text!")

# ----

window = Tk()

# ---- images
openImage = PhotoImage(file="C:\\Users\\hentg\\Desktop\\randomshit\\openfolder.png")
saveImage = PhotoImage(file="C:\\Users\\hentg\\Desktop\\randomshit\\save.png")
exitImage = PhotoImage(file="C:\\Users\\hentg\\Desktop\\randomshit\\exit.png")


# ----

menubar = Menu(window)
window.config(menu=menubar)

# ---- FileMenu for Open file, Save file, Exit file.

fileMenu = Menu(menubar, tearoff=0, font=("Red Hat Mono", 9))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=OpenFile, image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=SaveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound=LEFT)

# ----

# ---- EditMenu for Cut, Copy and Paste.

editMenu = Menu(menubar, tearoff=0, font=("Red Hat Mono", 9))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

# ----

window.mainloop()