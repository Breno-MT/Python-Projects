from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
VelocityX = 3
VelocityY = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

space_image = PhotoImage(file="C:\\Users\\hentg\\Documents\\Lightshot\\Screenshot_10.png")
background = canvas.create_image(0,0,image=space_image, anchor=NW)

ufo_image = PhotoImage(file="C:\\Users\\hentg\\Documents\\Lightshot\\Screenshot_8.png")
my_image = canvas.create_image(0,0,image=ufo_image, anchor=NW)


image_width = ufo_image.width()
image_height = ufo_image.height()



while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    
    if(coordinates[0]>= (WIDTH-image_width) or coordinates[0]< 0):
        VelocityX = -VelocityX
    if(coordinates[1]>= (HEIGHT-image_height) or coordinates[1]<0):
        VelocityY = -VelocityY
    
    canvas.move(my_image, VelocityX, VelocityY)
    window.update()
    time.sleep(0.01)


window.mainloop()