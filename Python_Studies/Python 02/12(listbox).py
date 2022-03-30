# list box = A listing of selectable text items within it's own container

from tkinter import * 


def delete():
    
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

def submit():
    
    food= []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have orderd: ")
    #print(listbox.get(listbox.curselection()))

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg = "#f7ffde",
                  font = ("Constantia",35),
                  width= 12,
                  selectmode=MULTIPLE,
                  )
listbox.pack()


listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())


entry_box = Entry(window)
entry_box.pack()

add_button = Button(window, 
                    text="add", 
                    command=add)
add_button.pack()




submit_button = Button(window,
                       text = "submit",
                       command=submit)
submit_button.pack()


delete_button = Button(window, text="delete", command=delete)
delete_button.pack()





window.mainloop()