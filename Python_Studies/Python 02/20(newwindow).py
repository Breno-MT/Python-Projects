from tkinter import *

def create_window():
    new_window = Tk()       # Toplevel() = new window "on top" of other windows, linked to a "bottom" window
                            # Tk() = a independent window
    old_window.destroy()    # close out of old window 



old_window = Tk()


Button(old_window, text="create a new window", command=create_window).pack()




old_window.mainloop()