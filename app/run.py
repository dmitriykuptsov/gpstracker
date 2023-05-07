#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
from utils import args

args = args.parse("config.dat")

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("1280x1280")

#Create a canvas
canvas= Canvas(win, width=1280, height=1280)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open(args["map"]))

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)

win.mainloop()

