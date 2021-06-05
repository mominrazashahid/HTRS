import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import hand
import checkout
import PySimpleGUI as sg
import imghdr
from doctest import master
from sys import path
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.filedialog import askopenfile
import goslate
from gingerit.gingerit import GingerIt
from googletrans import Translator
from textblob import TextBlob
from methods import Mytranslator
from collections import Counter
from urllib.request import urlopen
import SpeeckToText
import pycountry
import count
from doctest import master
from sys import path
from methods import Mytranslator
from collections import Counter
from tkinter import messagebox
import SpeeckToText
from PIL import ImageTk,Image
import time
from tkinter.ttk import *


window = ThemedTk(theme="arc")
def imagetotext():

    # window.iconify()
    windowhand =ThemedTk(theme="arc")

    def goback():
        windowhand.withdraw()
        import mainWIndow

    comsatframe = ttk.Frame(windowhand)
    comsatframe.pack(fill=BOTH)
    comsatlabel = ttk.Label(comsatframe, text='Comsat University Islamabad, Sahiwal', font=("Courier", 30, 'bold'),
                        )
    comsatlabel.pack(side=LEFT, pady=30, padx=(100, 5))
    img = Image.open(("../assets/Comsat.png"))
    photo = ImageTk.PhotoImage(img, master=windowhand)
    # img = ImageTk.PhotoImage(Image.open("com.jpg"))
    panel = ttk.Label(comsatframe, image=photo)
    panel.image = photo
    panel.pack(side=LEFT)
    # panel.place(x=1000)
    frame = ttk.Frame(windowhand, height=5)
    frame.pack(fill=X)
    x = "sample.png"
    label = ttk.Label(
        frame,
        text="Handwritten Image to text",


    )
    label.config(font=("Courier", 20, 'bold'))
    label.pack()

    Note = ttk.Label(
        frame,
        text="note: Handwritten text should be easy to readable and image should not be blur and A4 paper size image",


    )
    Note.config(font=("Courier", 15,))
    Note.pack()

    def openfilename():
        filename = filedialog.askopenfilename(title='Upload Image')

        return filename

    def open_img():
        global InputImage

        InputImage = openfilename()
        image_type = imghdr.what(InputImage)
        if not image_type:
            tk.messagebox.showinfo(title='File Info', message='please upload file only JPG or PNG')

        ImageAddress.config(text=os.path.basename(InputImage))
        # opens the image
        img = Image.open(InputImage)
        # resize the image and apply a high-quality down sampling filter
        img = img.resize((350, 450), Image.ANTIALIAS)
        img = img.save("NewImage.jpg")
        img2 = Image.open("NewImage.jpg")
        # img2 = ImageTk.PhotoImage(Image.open("NewImage.jpg"))
        img3 = ImageTk.PhotoImage(img2, master=windowhand)
        panel.configure(image=img3)
        panel.image = img3
        tk.messagebox.showinfo(title='File Info', message='File Uplaod successfully')
        windowhand.lift()


        # set the image as img

    img = Image.open(("com.jpg"))
    photo = ImageTk.PhotoImage(img, master=windowhand)
    # img = ImageTk.PhotoImage(Image.open("com.jpg"))
    panel = ttk.Label(windowhand, image=photo)
    panel.image = photo
    panel.pack()
    panel.place(x=200, y=270)

    ImageAddress = ttk.Label(
        windowhand,
        text=x,

    )
    ImageAddress.config(font=("Courier", 10))
    ImageAddress.pack()
    ImageAddress.place(x=200, y=730)
    text = Text(windowhand, width=100, height=10)
    text.pack()
    text.place(x=580, y=260)




    def recognize_text():
        try:
            progress['value'] = 10
            windowhand.update_idletasks()
            time.sleep(1)
            hand.create_image(InputImage)
            progress['value'] = 40
            windowhand.update_idletasks()
            time.sleep(1)
            checkout.check(InputImage)
            progress['value'] = 70
            windowhand.update_idletasks()
            time.sleep(1)
            from src import Main
            Text_Recognized = Main.text_recognized
            abc = ' '.join(Text_Recognized)
            progress['value'] = 100
            windowhand.update_idletasks()
            time.sleep(1)
            text.delete(1.0, END)
            text.insert(END, abc)
            progress['value'] = 0
            windowhand.update_idletasks()
            time.sleep(1)

        except Exception as e:

            tk.messagebox.showinfo(title='File Info', message='Error:' + str(e))

    def Save_File():
        try:
            save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if save_text_as:
                text_to_save = text.get("1.0", END)
                save_text_as.write(text_to_save)
                save_text_as.close()
                tk.messagebox.showinfo(title='File Info', message='File save successfully')

            else:

                messagebox.showinfo("Error", "Cancelled")
                windowhand.lift()
        except Exception as e:
            tk.messagebox.showinfo(title='System say', message='' + str(e))

    progress = Progressbar(windowhand, orient=HORIZONTAL, length=150, mode='determinate')
    progress.pack(side="left")
    progress.place(x=600, y=460)


    btn = ttk.Button(windowhand, text='Upload Image', command=open_img)
    btn.pack(side="left")
    btn.place(x=800, y=450)
    btn1 = ttk.Button(windowhand, text='Start Recognition', command=recognize_text)
    btn1.pack()
    btn1.place(x=950, y=450)

    btn2 = ttk.Button(windowhand, text='Save file', command=Save_File)
    btn2.pack()
    btn2.place(x=1100, y=450)

    menubar = Menu(windowhand)
    filemenu =Menu(menubar, tearoff=0)
    filemenu.add_command(label="upload image", command=open_img)

    filemenu.add_separator()
    def quit():
        windowhand.withdraw()
        window.deiconify()

    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=open_img)

    editmenu.add_separator()
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=open_img)
    helpmenu.add_command(label="About...", command=open_img)
    menubar.add_cascade(label="Help", menu=helpmenu)
    windowhand.config(menu=menubar)
    windowhand.config(bg="#F5F6F8")
    windowhand.minsize(1400, 800)
    windowhand.mainloop()


def translator():
    app = ThemedTk(theme="arc")

    def goback():
        app.withdraw()
        import mainWIndow

    def getSpeechtoText():
        getInputLnaguage = Inputlangs.get()

        text = SpeeckToText.speech_to_text(getInputLnaguage[0:2])

        if text == "Sphinx could not understand audio":

            tk.messagebox.showinfo(title='Error', message='Could not understand your voice')
            app.lift()
        elif text == "error":
            tk.messagebox.showinfo(title='Error', message='some error make sure you have internet connecition!')
            app.lift()
        else:

            inputtextbox.delete(1.0, END)
            inputtextbox.insert(END, text)

    mytranslator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr', ])

    def get():
        # try:

        d = desLangs.get()

        inputtext = inputtextbox.get(1.0, END)

        if len(inputtextbox.get("1.0", "end-1c")) == 0:
            tk.messagebox.showinfo(title='Error', message='Input Text area is empty')
            app.lift()
        else:

            mytrans = mytranslator.translate([inputtext], dest=d)
            for translation in mytrans:

                destText.delete(1.0, END)
                destText.insert(END, translation.text)
        # except:
        #     tk.messagebox.showinfo(title='Error', message='Make sure you have internet connection!')
        #     app.lift()
    def open():

        file = askopenfile(mode='r', filetypes=[('', '.txt')])
        if file is not None:
            content = file.read()
            inputtextbox.delete(1.0, END)
            inputtextbox.insert(END, content)

    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.overrideredirect(0)
    app.config()
    app.wm_iconbitmap('favicon (1).ico')
    app.title('htr-gr system')
    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open", command=open)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save as...")
    filemenu.add_command(label="Close")
    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo")
    editmenu.add_separator()
    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    editmenu.add_command(label="Delete")
    editmenu.add_command(label="Select All")
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="About...")
    menubar.add_cascade(label="Help", menu=helpmenu)
    app.config(menu=menubar)
    comsatframe = ttk.Frame(app)
    comsatframe.pack(fill=BOTH)
    comsatlabel = ttk.Label(comsatframe, text='Comsat University Islamabad, Sahiwal', font=("Courier", 30, 'bold'))
    comsatlabel.pack(side=LEFT, pady=30, padx=(100, 5))
    img = Image.open(("../assets/Comsat.png"))
    photo = ImageTk.PhotoImage(img, master=app)
    panelImage = ttk.Label(comsatframe, image=photo)
    panelImage.pack(side=LEFT)
    frame = ttk.Frame(app)
    frame.pack(fill=BOTH, pady=50)
    appName = ttk.Label(frame, text='English to Urdu translation', font=('Sans Serif', 20, 'bold'))
    appName.pack(fill=X, side=LEFT, padx=100)
    frame1 = ttk.Frame(app)
    frame1.pack(fill=BOTH)
    inputlablel = ttk.Label(frame1, text='Input text', font=('Sans Serif', 15))
    inputlablel.pack(side=LEFT, padx=(100, 2), pady=5)
    language_auto_Detect = ttk.Label(frame1, text='(Input languge auto detected)', font=('Sans Serif', 15))
    language_auto_Detect.pack(side=LEFT)
    correctlabel = ttk.Label(frame1, text='Translated text', font=('Sans Serif', 15))
    correctlabel.pack(side=LEFT, padx=370, fill=X)
    inputtextframe = ttk.Frame(app)
    inputtextframe.pack(fill=BOTH)
    inputtextbox = Text(inputtextframe, font=('calibri', 12), width=50, height=10)
    inputtextbox.pack(side=LEFT, padx=(100, 80))
    langs = Mytranslator().langs
    desLangs = ttk.Combobox(inputtextframe, values=langs, width=8)
    desLangs.set("urdu")
    desLangs.pack(side=LEFT)
    transbtn = ttk.Button(inputtextframe, text='Translate', command=get)
    transbtn.pack(side=LEFT, padx=10)
    destText = Text(inputtextframe, font=('calibri', 12), width=50, height=10)
    destText.pack(side=LEFT, padx=80)
    inputlansframe = ttk.Frame(app)
    inputlansframe.pack(fill=BOTH)
    Inputlangs = ttk.Combobox(inputlansframe, values=count.allcountry(), width=8)
    Inputlangs.set('ur Urdu')
    Inputlangs.pack(side=LEFT, padx=(100, 10))
    transbtn = ttk.Button(inputlansframe, text='Click and speak', command=getSpeechtoText)
    transbtn.pack(side=LEFT, padx=10)
    NoteFrame = ttk.Frame(app)
    NoteFrame.pack(fill=BOTH, pady=20)
    Notelabel = ttk.Label(NoteFrame, text='Note: After click on', font=('Sans Serif', 12))
    Notelabel.pack(fill=X, side=LEFT, padx=(100, 0))
    Notelabel1 = ttk.Label(NoteFrame, text='click and speak', font=('Sans Serif', 12))
    Notelabel1.pack(fill=X, side=LEFT)
    Notelabel2 = ttk.Label(NoteFrame, text='button wait for 1 second then speak for better result', font=('Sans Serif', 12),
                       )
    Notelabel2.pack(fill=X, side=LEFT)
    BackFrame = ttk.Frame(app)
    BackFrame.pack(fill=BOTH)
    app.config(bg="#F5F6F8")
    app.minsize(1400,700)
    app.mainloop()


def GrammerChecker():
    gram_app = ThemedTk(theme="arc")

    def getSpeechtoText():
        getInputLnaguage = "En"
        text = SpeeckToText.speech_to_text(getInputLnaguage)
        if text == "Sphinx could not understand audio":
            tk.messagebox.showinfo(title='Error', message='Could not understand your voice')
            gram_app.lift()
        elif text == "error":
            tk.messagebox.showinfo(title='Error', message='some error make sure you have internet connecition!')
            gram_app.lift()
        else:
            inputtextbox.delete(1.0, END)
            inputtextbox.insert(END, text)



    mytranslator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr', ])

    def color_text(edit, tag, word, fg_color='black', bg_color='white'):
        # add a space to the end of the word
        word = word + " "
        edit.insert('end', word)
        end_index = edit.index('end')
        begin_index = "%s-%sc" % (end_index, len(word) + 1)
        edit.tag_add(tag, begin_index, end_index)
        edit.tag_config(tag, foreground=fg_color, background=bg_color)

    def scan():
        try:
            inputtext = inputtextbox.get(1.0, END)
            if len(inputtextbox.get("1.0", "end-1c")) == 0:
                tk.messagebox.showinfo(title='Error', message='Input Text area is empty')
                gram_app.lift()
            else:
                inputList = list(inputtext.split(" "))
                g = GingerIt()
                g1 = g.parse(inputtext)['result']
                correctList = list(g1.split(" "))
                correcttextbox.delete(1.0, END)
                correcttextbox.insert(END, g1)
                correct = g.parse(inputtext)["corrections"]
                correct.reverse()
                error_index = []
                error_words = []
                correct_word = []
                count = 0
                for i in correct:
                    count = count + 1
                for j in range(count):
                    item1 = correct[j]
                    error_index.append(item1["start"])
                    error_words.append(item1["text"])
                    correct_word.append(item1["correct"])
                Highlight_text(error_index, error_words, correct_word, g1)
        except:
            tk.messagebox.showinfo(title='Error', message='some error make sure you have internet connecition!')
            gram_app.lift()

    def split(word):
        return [char for char in word]

    def Highlight_text(index, ErrorWord, Correctword, g1):
        Index = index
        errorword = ErrorWord
        correctword = Correctword
        total_error = len(index)
        for i in range(total_error):
            INDEX = Index[i]
            string = errorword[i]
            intstring = len(string)
            totat_length = INDEX + intstring
            startindex = "1." + str(Index[i])
            endindex = "1." + str(totat_length)
            inputtextbox.tag_add("here", startindex, endindex)
            inputtextbox.tag_config("here", background="#F13B3E", foreground="black")
        for i in range(total_error):
            INDEX = Index[i]
            string = correctword[i]
            intstring = len(string)
            commas = CheckCommas(INDEX, g1)
            totat_length = INDEX + commas + intstring
            startindex = "1." + str(Index[i])
            endindex = "1." + str(totat_length)
            correcttextbox.tag_add("here", startindex, endindex)
            correcttextbox.tag_config("here", background="#4FE256", foreground="black")

    def CheckCommas(indexNo, text):
        count = 0
        for i in range(indexNo):
            substring = ","
            count = text.count(substring)
        return count

    def open():

        file = askopenfile(mode='r', filetypes=[('', '.txt')])
        if file is not None:
            content = file.read()
            inputtextbox.delete(1.0, END)
            inputtextbox.insert(END, content)


    # w, h = Gapp.winfo_screenwidth(), Gapp.winfo_screenheight()
    # Gapp.overrideredirect(0)
    # Gapp.config()
    gram_app.wm_iconbitmap('favicon (1).ico')
    gram_app.title('htr-gr system')
    menubar = Menu(gram_app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open", command=open)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save as...")
    filemenu.add_command(label="Close")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=gram_app.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo")
    editmenu.add_separator()
    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    editmenu.add_command(label="Delete")
    editmenu.add_command(label="Select All")
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="About...")
    menubar.add_cascade(label="Help", menu=helpmenu)
    gram_app.config(menu=menubar)
    comsatframe = ttk.Frame(gram_app)
    comsatframe.pack(fill=BOTH)
    comsatlabel = ttk.Label(comsatframe, text='Comsat University Islamabad, Sahiwal', font=("Courier", 30, 'bold'),)
    comsatlabel.pack(side=LEFT, pady=30, padx=(100, 5))
    img = Image.open(("../assets/Comsat.png"))
    photo = ImageTk.PhotoImage(img, master=gram_app)
    # img = ImageTk.PhotoImage(Image.open("com.jpg"))
    panel =ttk.Label(comsatframe, image=photo)
    panel.image = photo
    panel.pack(side=LEFT)
    frame = ttk.Frame(gram_app)
    frame.pack(fill=BOTH)
    gram_app1 = ttk.Label(frame, text='Grammer mistake remover', font=('Sans Serif', 20, 'bold'))
    gram_app1.pack(fill=X, side=LEFT, padx=100)
    frame1 = ttk.Frame(gram_app)
    frame1.pack(fill=BOTH)
    inputlablel = ttk.Label(frame1, text='Input text', font=('Sans Serif', 15))
    inputlablel.pack(side=LEFT, padx=(100, 2), pady=5)
    language_auto_Detect = ttk.Label(frame1, text='(Input languge English only)', font=('Sans Serif', 15))
    language_auto_Detect.pack(side=LEFT)
    correctlabel = ttk.Label(frame1, text='Corrected text', font=('Sans Serif', 15))
    correctlabel.pack(side=LEFT, padx=370, fill=X)
    inputtextframe = ttk.Frame(gram_app)
    inputtextframe.pack(fill=BOTH)
    inputtextbox = Text(inputtextframe, font=('calibri', 12), width=50, height=10)
    inputtextbox.pack(side=LEFT, padx=(100, 80))
    langs = Mytranslator().langs
    transbtn = ttk.Button(inputtextframe, text='Check mistake', command=scan)
    transbtn.pack(side=LEFT, padx=10)
    correcttextbox = Text(inputtextframe, font=('calibri', 12), width=50, height=10)
    correcttextbox.pack(side=LEFT, padx=80)
    inputlansframe = ttk.Frame(gram_app)
    inputlansframe.pack(fill=BOTH)
    inputlansframe = ttk.Frame(gram_app)
    inputlansframe.pack(fill=BOTH)
    transbtn = ttk.Button(inputlansframe, text='Click and speak', command=getSpeechtoText)
    transbtn.pack(side=LEFT, padx=100)
    NoteFrame = ttk.Frame(gram_app)
    NoteFrame.pack(fill=BOTH)
    Notelabel = ttk.Label(NoteFrame, text='Note: After click on', font=('Sans Serif', 12))
    Notelabel.pack(fill=X, side=LEFT, padx=(100, 0))
    Notelabel1 = ttk.Label(NoteFrame, text='click and speak', font=('Sans Serif', 12))
    Notelabel1.pack(fill=X, side=LEFT)
    Notelabel2 = ttk.Label(NoteFrame, text='button wait for 1 second then speak for better result', font=('Sans Serif', 12))
    Notelabel2.pack(fill=X, side=LEFT)
    BackFrame = ttk.Frame(gram_app)
    BackFrame.pack(fill=BOTH)
    gram_app.config(bg="#F5F6F8")
    gram_app.minsize(1300,600)
    gram_app.mainloop()



frame=ttk.Frame(window)
frame.pack(fill=X)
label = ttk.Label(
    frame,
    text="Comsat University Islamabad, sahiwal",
)
label.config(font=("Courier",30,'bold'))
label.pack(side=LEFT,padx=(100,30))
img=Image.open(("../assets/Comsat.png"))
photo = ImageTk.PhotoImage(img,master=window)
panelImage = ttk.Label(frame, image=photo)
panelImage.pack(side=LEFT)
htr= ttk.Label(
    window,
    text="Welcome to HTR-GR system",

)
htr.config(font=("Courier",20,'bold'))
htr.pack()
NoteData= ttk.Label(
    window,
    text="Note: This project is build in python using artifiical  Intelligence  we  train  complete model \n        which recognize  handwritten text from image and further remove grammatical mistake and \n        translate into different langauge.",

)
NoteData.config(font=("Courier",15))
NoteData.pack(pady=40)
Icio_frame=ttk.Frame(window)
Icio_frame.pack(pady=50)


img=Image.open(("../assets/TextRecognize.png"))
recognitionImage = ImageTk.PhotoImage(img,master=window)
recognition_Image = ttk.Label(Icio_frame, image=recognitionImage)
recognition_Image.pack(side=LEFT,padx=(0,130))

img=Image.open(("../assets/trans.png"))
TransImage = ImageTk.PhotoImage(img,master=window)
Trans_Image = ttk.Label(Icio_frame, image=TransImage)
Trans_Image.pack(side=LEFT,padx=(0,130))


img=Image.open(("../assets/Grammer.png"))
image = ImageTk.PhotoImage(img,master=window)
TextRecignizeIMG2 = ttk.Label(Icio_frame, image=image)
TextRecignizeIMG2.pack(side=LEFT)
frame_button= ttk.Frame(window)
frame_button.pack(pady=0)

b1=ttk.Button(frame_button,text="Handwritten Image to text",command=imagetotext)
b1.pack(side=LEFT,padx=40,pady=0)
b2=ttk.Button(frame_button,text="Translator",command=translator)
b2.pack(side=LEFT,padx=120,pady=0,)
b3=ttk.Button(frame_button,text="Grammatical Mistake remover",command=GrammerChecker)
b3.pack(side=LEFT,padx=30,pady=0,)
Reg=ttk.Frame(window)
Reg.pack(fill=BOTH,pady=10)
groupmember = ttk.Label(
Reg,
    text="Group Members are:   Moman Raza              saboor Afzal          Waleed Raza",


)
groupmember.config(font=("Courier",15,'bold'))
groupmember.pack(fill=X,padx=110,pady=30)
groupmemberReg = ttk.Label(
Reg,
    text="                              Fa16-BCS-157            FA16-BCS-158          Fa16-BCS-148",




)
groupmemberReg.config(font=("Courier",15,'bold'))
groupmemberReg.pack(fill=X)

window.configure(bg="#F5F6F8")
window.minsize(1400,800)
window.mainloop()