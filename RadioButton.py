from tkinter import *
import tkinter.messagebox as tmsg

r=Tk()
r.geometry("430x530")
r.title("Radio_Button learning")
def submit():
    a = tmsg.askyesno("Confirm order",f"We recieved order request for {var.get()} \n Cofirm Order ?")
    print(a)
    b = (var.get())
    print(b)
    if a == 1:
        b = tmsg.showinfo("Msg from A_B_ Foods", "Your bill is on Akash sethji, enjoy the meal :)")


Label(text="A_B_ foods", font= "lucida 19 bold", relief= SUNKEN,bg="light grey", borderwidth=6, padx=15, pady=10).pack(padx=10, pady=10, side= TOP)

var = StringVar()
var.set(1)
Label(text="What would you like to Order ?", font= "comicsansms 14 bold", relief= SUNKEN, borderwidth=6, padx=15, pady=10).pack(padx=10, pady=10, side= TOP)
a = Radiobutton (r, text= "Burger", variable= var, value="Burger").pack()
a = Radiobutton (r, text= "Vada Pav", variable= var, value="Vada Pav").pack()
a = Radiobutton (r, text= "Oreo shake", variable= var, value="Oreo shake").pack()
a = Radiobutton (r, text= "Soda lime", variable= var, value="Soda lime").pack()



Button(text="Order Now",font = " Arial 14 italic", borderwidth=3, relief =RAISED, pady=5, padx=10, command=submit).pack(padx=10, pady = 13)

photo = PhotoImage(file="AB_food.png")
akash = Label(image=photo)
akash.pack(side=BOTTOM)

r.mainloop()