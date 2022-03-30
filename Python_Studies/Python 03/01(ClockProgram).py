from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S") # STR Hours: Minutes: Seconds
    time_label.config(text=time_string) # Sets texts to time_string (will appear Hours: Minutes: Seconds)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)


    window.after(1000, update)

window = Tk()

time_label = Label(window, font=("Arial", 15), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Consolas", 9))
day_label.pack()

date_label = Label(window, font=("Comic Sans", 20))
date_label.pack()


update()


window.mainloop()