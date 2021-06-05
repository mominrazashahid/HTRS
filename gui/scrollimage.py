# from tkinter import *
#
# # loading Python Imaging Library
# from PIL import ImageTk, Image
#
# # To get the dialog box to open when required
# from tkinter import filedialog
# # Create a windoe
# root = Tk()
#
# # Set Title as Image Loader
# root.title("Image Loader")
#
# # Set the resolution of window
# root.geometry("550x300")
#
# # Allow Window to be resizable
# root.resizable(width = True, height = True)
#
# # Create a button and place it into the window using grid layout
# def openfilename():
#
# 	# open file dialog box to select image
# 	# The dialogue box has a title "Open"
# 	filename = filedialog.askopenfilename(title ='"pen')
# 	return filename
#
# def open_img():
#     # Select the Imagename from a folder
#     x = openfilename()
#
#     # opens the image
#     img = Image.open(x)
#
#     # resize the image and apply a high-quality down sampling filter
#     img = img.resize((250, 250), Image.ANTIALIAS)
#
#     # PhotoImage class is used to add image to widgets, icons etc
#     img = ImageTk.PhotoImage(img)
#
#     # create a label
#     panel = Label(root, image=img)
#
#     # set the image as img
#     canvas = Canvas(root, width=300, height=300)
#     canvas.pack()
#     img = PhotoImage(file="ball.ppm")
#     canvas.create_image(20, 20, anchor=NW, image=img)
#

#
# btn = Button(root, text ='open image', command = open_img).grid(
# 										row = 1, columnspan = 4)
# root.mainloop()
#
#

# --- functions ---
import tkinter as tk
from PIL import ImageTk,Image
def on_click():
    # change image on canvas
    canvas.itemconfig(image_id, image=image2)

# --- main ---

root = tk.Tk()

# canvas for image
canvas = tk.Canvas(root, width=60, height=60)
canvas.pack()

# button to change image
button = tk.Button(root, text="Change", command=on_click)
button.pack()

# images
image1 = ImageTk.PhotoImage(Image.open("def.jpg"))
image2 = ImageTk.PhotoImage(Image.open("main.jpg"))

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=image1)

root.mainloop()