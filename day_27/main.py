import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text = "I am a label.", font=("Arial", 16, "bold"))
my_label.pack() # displays it on screen

# Advanced python arguments

# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.

# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.

def show_me(*args):
    for n in args:
        print(n)

show_me(1,3,4,2,5,7,"the","money")




window.mainloop()