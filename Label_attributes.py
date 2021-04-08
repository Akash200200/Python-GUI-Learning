from tkinter import *

root = Tk ()
#GUI logic here
root.geometry('740x350')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(1500,600)     # (width, hieght)
root.title ("Akash's GUI")

# important Label options
#text = adds the text
#bd = background
#fg = foreground
#font = sets the font 1.font = ("times new roman", 16, "bold") 2.font ="times new roman" 16 "bold"
#padx = x padding
#pady = y padding
#borderwidth = gives border
#relief = border styling (SUNKEN, RAISED, GROOVE, RIDGE)

rohit = Label (text = "Rohit Gurunath Sharma (born 30 April 1987) \nis an Indian international cricketer who plays for \nMumbai in domestic cricket and captains Mumbai Indians in the\n Indian Premier League as a right-handed batsman and an\n occasional right-arm off break bowler. He is the \nvice-captain of the Indian national team in limited-overs for\nmats. He is one of the most decorated contemporary \nbatsmen in the limited-overs format of the game.", bg = "black", fg = "white", padx=5, pady=100, font ="comicsansms 16 bold", borderwidth=10, relief= RIDGE)
rohit.pack()

root.mainloop()