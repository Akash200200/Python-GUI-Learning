from tkinter import *
import tkinter.messagebox as tmsg

r=Tk()
r.geometry("300x300")
r.title("Submenu Learning")

def profile():
    c= tmsg.showinfo("Choose Profile", "There is No profile created ")

def project():
    c= tmsg.askyesno("Choose project", "There is No project created, would you like to create new?")
    print(c)

def save():
    c= tmsg.askokcancel("save Current Data ?", "Do you wish to save the Current data ?")
    print(c)

def preview():
    c= tmsg.showinfo("Preview", "Preview unvailable")

def font():
    print("select font Style")
    b = tmsg.showinfo("Select your favourate font style", "No font style available, come back later !")

def size():
    print("select font Size")
    b= tmsg.askquestion("Check font size","Is this font size enough ?")
    print(b)


def appearance():
    print("Theme availability Checked by Costumer")
    b= tmsg.showinfo("Want to Change theme ?", "Sorry, only light theme is available right now.")


def help():
    b= tmsg.showinfo("Need any help ?", "Help yourself, Google it !!!")
    print(b)

def meal():
    print("Meal Availability Checked")
    a= tmsg.askyesno("Meal Requirement", "Would you like to have meal in your Journey ?")
    print(a)

def code():
    print("Coupon Availability Checked")
    a= tmsg.askyesno("Coupon Code use", "Do you Want to use your First time coupon code ?")
    print(a)

def support():
    print("Equiry approached")
    a= tmsg.askokcancel("Enquiry needed", "Give us a call? -> 9359109196")
    print(a)

def fb():
    print("Feedback option checked by costomer")
    a= tmsg.askyesno("Tell us about your experience", "was your experience good ?")
    print(a)


mainmenu = Menu(r)
m1 = Menu (mainmenu, tearoff=0)
m1.add_command(label="Profile", command=profile)
m1.add_command(label="Project", command=project)
m1.add_separator()
m1.add_command(label="Save as", command=save)
m1.add_command(label="Preview", command=preview)
r.config(menu=mainmenu)
mainmenu.add_cascade(label="Open", menu=m1)


m2 = Menu (mainmenu, tearoff=0)
m2.add_command(label="Font", command=font)
m2.add_command(label="Size", command=size)
m2.add_command(label="Appearance", command=appearance)
m2.add_separator()
m2.add_command(label="Help", command=help)

r.config(menu=mainmenu)
mainmenu.add_cascade(label="Setting", menu=m2)

m3 = Menu (mainmenu, tearoff=0)
m3.add_command(label="Meal", command=meal)
m3.add_command(label="Coupon", command=code)
m3.add_command(label="Enquiry", command=support)
m3.add_separator()
m3.add_command(label="Feedback", command=fb)

r.config(menu=mainmenu)
mainmenu.add_cascade(label="Services", menu=m3)


r.mainloop()