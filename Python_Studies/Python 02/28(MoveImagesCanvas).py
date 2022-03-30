from tkinter import *

def Move_Up(event):
    canvas.move(myImage,0,-10)

def Move_Down(event):
    canvas.move(myImage,0,10)

def Move_Right(event):
    canvas.move(myImage,10, 0)

def Move_Left(event):
    canvas.move(myImage, -10, 0)



window = Tk()

window.bind("<w>", Move_Up)
window.bind("<s>", Move_Down)
window.bind("<d>", Move_Right)
window.bind("<a>", Move_Left)



canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoImage = PhotoImage(file="C:\\Users\\hentg\\Documents\\Lightshot\\Screenshot_7.png")
myImage = canvas.create_image(0,0, image=photoImage, anchor=NW)

window.mainloop()