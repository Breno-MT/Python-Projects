from tkinter import *

def doSomething(event):
    print("You did a thing!" + str(event.x) + "," + str(event.y))


window = Tk()

window.bind("<Button-1>", doSomething) # Button-1 "Left Click"
# window.bind("<Button-2>", doSomething) # Button-2 "Middle Click; Scroll"
# window.bind("<Button-1>", doSomething) # Button-3 "Right click"
# window.bind("<ButtonRelease>", doSomething) # ButtonRelease the mouse click to show something or do something
# window.bind("<Enter>", doSomething) # Enter the window
# window.bind("<Leave>", doSomething) # Leave the window
# window.bind("<Motion>", doSomething) # Where the mouse moved

window.mainloop()