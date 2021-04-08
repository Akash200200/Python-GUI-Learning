from tkinter import *

root = Tk ()
#GUI logic here
root.geometry('740x350')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(1500,900)     # (width, hieght)
root.title ("Jai Shree Ram")

rohit = Label (text = "Rohit Gurunath Sharma (born 30 April 1987) \nis an Indian international cricketer who plays for \nMumbai in domestic cricket and captains Mumbai Indians in the\n Indian Premier League as a right-handed batsman and an\n occasional right-arm off break bowler. He is the \nvice-captain of the Indian national team in limited-overs for\nmats. He is one of the most decorated contemporary \nbatsmen in the limited-overs format of the game.", bg = "black", fg = "white", padx=50, pady=60, font ="comicsansms 16 bold", borderwidth=3, relief= RIDGE)

#important pack attribute
#anchor = nw, ne
#side = top,bottom,left,right
#fill = X,Y
#padx =
#pady =

#rohit.pack(side=TOP, fill=X, padx=30, pady=30)    # fill attribute workking
rohit.pack(side=LEFT, fill=X, padx=25, pady= 25)   # fill not working ... i dont know y ?

root.mainloop()

# info = Label (text = "He is the best. Most loved by his mother and father who also have 2 more children but they hate the other two as they are disobidient.", Font="comicsansms 14 bold", bg = "black", fg= "white", borderwidth= 5, relief =SUNKEN, padx=15, pady= 15)