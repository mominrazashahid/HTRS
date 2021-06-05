import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from src import hand
from src import checkout
window = tk.Tk()
x="abc"
label = tk.Label(
    text="HTR, GR system",
    fg="black",
    bg="#a0a6b0",
    width=200,
    height=3,

)
label.config(font=("Courier",40,'bold'))
label.pack()

def openfilename():

	# open file dialog box to select image
	# The dialogue box has a title "Open"
	filename = filedialog.askopenfilename(title ='"pen')

	return filename

def open_img():
    # Select the Imagename from a folder\
    global x

    x = openfilename()



    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((350, 450), Image.ANTIALIAS)
    img = img.save("com.jpg")
    img2 = ImageTk.PhotoImage(Image.open("D:\momin fyp\codes\combing codes\gui\com.jpg"))
    panel.configure(image=img2)
    panel.image = img2



    # set the image as img

img = ImageTk.PhotoImage(Image.open("D:\momin fyp\codes\combing codes\gui\com.jpg"))
panel = tk.Label(window, image=img)
panel.pack()
panel.place(x=200,y=200)
text = Text(window,width=100,height=10)
text.pack()
text.place(x=580,y=200)

btn = Button(window, text ='Upload Image',padx=20, pady=20, command =open_img)
btn.pack(side="left")
btn.place(x=800,y=400)


def recognize_text():
    hand.create_image(x)
    checkout.check(x)







btn1 = Button(window, text ='Recognize text', padx=20, pady=20, command =recognize_text)
btn1.pack()
btn1.place(x=950,y=400)


# text.place(x=1150,y=200)






menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="upload image", command=open_img)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=open_img)

editmenu.add_separator()

# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)

# menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=open_img)
helpmenu.add_command(label="About...", command=open_img)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.geometry("1900x1500")
window.mainloop()
