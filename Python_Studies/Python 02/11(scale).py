from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get()) + " degree C")


window = Tk()

window.geometry("520x1200")


hot_image = PhotoImage(file="C:\\Users\\hentg\\Desktop\\hot.png")
hot_Label = Label(image=hot_image)
hot_Label.pack()


scale = Scale(window, 
              from_=100,
              to=0,
              length = 600,
              orient=VERTICAL, # orientation of scale
              font = ("Roboto", 15),
              tickinterval= 10, # adds numeric indicators for value
              showvalue=0, # hide current value
              resolution= 5, # increment of slider
              troughcolor="#93c9c8",
              fg = "#FF1C00",
              bg = "black",
              )

scale.set(((scale["from"]-scale["to"])/2)+scale["to"]) # set current value of slider
scale.pack()

ice_image = PhotoImage(file="C:\\Users\\hentg\\Desktop\\ice.png")
ice_Label = Label(image=ice_image)
ice_Label.pack()


button = Button(window, 
                text= "Submit", 
                command=submit)
button.pack()
window.mainloop()