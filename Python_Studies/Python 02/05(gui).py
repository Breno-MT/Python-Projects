from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png') # só trocar pela imagem q usava, to com depressão
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events
