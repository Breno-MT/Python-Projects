from tkinter import *

def Move_Up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def Move_Down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def Move_Left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

def Move_Right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>",Move_Up)
window.bind("<s>",Move_Down)
window.bind("<a>",Move_Left)
window.bind("<d>",Move_Right)

window.bind("<Up>",Move_Up)
window.bind("<Down>",Move_Down)
window.bind("<Left>",Move_Left)
window.bind("<Right>",Move_Right)



myImage = PhotoImage(file="C:\\Users\\hentg\\Documents\\Lightshot\\Screenshot_7.png")

label = Label(window,image=myImage)
label.place(x=0, y=0)


window.mainloop()