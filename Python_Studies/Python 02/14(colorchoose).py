from tkinter import *
from tkinter import colorchooser # submodule


def click():
    
    window.config(bg=colorchooser.askcolor()[1])
    
    #color = colorchooser.askcolor()
    #window.config(bg=color[1])
    
    #colorHex = color[1]
    #window.config(bg=colorHex) # change bg color


window = Tk()
window.geometry("500x500")


button = Button(text="click me",command=click)
button.pack()





window.mainloop()