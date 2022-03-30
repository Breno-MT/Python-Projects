from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of window and displays

tab1 = Frame(notebook) # new frame for tab1
tab2 = Frame(notebook) # --- ----- --- tab2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()

Label(tab1, text="Hello, this is tab#1", width=50, height=25).pack()
Label(tab2, text="Goodbay, this is tab#2", width=50, height=25).pack()



window.mainloop()