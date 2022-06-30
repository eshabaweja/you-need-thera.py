from tkinter import *
# 1 mile = 1.6 km
#Creating a new window and configurations
window = Tk()
window.title("Miles - Kilometer Converter")
window.minsize(width=500, height=300)
window.grid()
window.config(padx=100, pady=150)

# miles
miles = Entry(width=10)
miles.grid(row=0,column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)

# is equal to
equal_label = Label(text="is equal to")
equal_label.grid(row=1,column=0)

# kilometers
kilometers = Label(text="0")
kilometers.grid(row=1,column=1)

km_label = Label(text="Kilometers")
km_label.grid(row=1,column=2)

# button
def to_km():
    kilometers.config(text=int(miles.get())*1.609)

calc_btn = Button(text="Calculate", command=to_km)
calc_btn.grid(row =2, column=1)

# end mainloop
window.mainloop()