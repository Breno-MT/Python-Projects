from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This is an info box", message="You are a person!")
    #messagebox.showwarning(title="This is an info box", message="You have VIRUS!!!")
    #messagebox.showerror(title="ERROR!", message="Something went wrong!")

    #if messagebox.askokcancel(title="Ask ok cancel", message="Do you want to do the thing?"):
        #print("You did a thing!")
    #else:
        #print("You canceled a thing!")
    
    #while True:
       # if messagebox.askretrycancel(title="Ask retry cancel", message="Do you want to retry the thing?"):
            #print("You retried a thing!")
        #else:
            #print("You canceled a thing!")
            #break
    #if messagebox.askyesno(title="ask yes or no", message="Do you like cake ?"):
        #print("I like cake too! :D")
   # else:
        #print("Why do you not like cake??? D:")
    
    #answer = messagebox.askquestion(title="Ask question", message="Do you like pie?")
    #if (answer == "yes"):
        #print("I like pie too! :D")
    #else:
        #print("Why you are such a monster? D:")
    
    #print(messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?")) # Returns True;Yes / False;No / None;Cancel
    answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?", icon="error")
    if(answer == True):
        print("You like to code! :D")
    elif(answer == False):
        print("Then why don't you go watch baby videos? >:(")
    else:
        print("You have dodge the question! :P")





window = Tk()

button = Button(window, command=click, text="click me")
button.pack()


window.mainloop()