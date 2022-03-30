# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburguer", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a hamburguer!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("Huh?")





window = Tk()

pizza_image = PhotoImage(file="C:\\Users\\hentg\\Desktop\\pizza.png")
hotdog_image = PhotoImage(file="C:\\Users\\hentg\\Desktop\\hotdog.png")
hamburguer_image = PhotoImage(file="C:\\Users\\hentg\\Desktop\\hamburguer.png")

food_images = [pizza_image, hamburguer_image, hotdog_image]

x = IntVar()


for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index], # adds text to the radio buttons
                               variable=x, # group radiobuttons together if they share the same variable
                               value=index, # assigns each radiobuttons a different value
                               padx = 25, # adds padding on x-axis
                               font = ("Impact", 15), # adds some fonts to the letters
                               image = food_images[index], # this adds image to the radio buttons
                               compound="left", # adds image & text ( left - side )
                               indicatoron=1, # eliminate circle indicators
                               width= 510, # sets width of radio buttons
                               command= order # this will set command of radio buttons to function
                               )
    radio_button.pack(anchor=W)


window.mainloop()