from firebase import firebase as fb
import piratedata
import firebasemanager
import imagemanager
from tkinter import*
import random
import os
from tkinter import filedialog
def addnew():
    global nBox, sBox, win, optionstring
    #create a new instance of pirate class
    p = piratedata.Pirate()
    #get values out of boxes
    #load into pirate
    p.name = nBox.get()
    p.ship = sBox.get()
    p.fictional = optionstring.get()
    #now upload the image and get  signed url back
    im = imagemanager.ImageManager()
    im.imagepath = win.filename
    im.uploadImage()
    p.image = im.url
    #clear boxes
    nBox.delete(0,"end")
    sBox.delete(0,"end")
    imgLabel.config(text = "")
    #generate dict
    d = p.getdict()
    #create new instance of file manager class
    f = firebasemanager.FirebaseManager()
    #generate random id
    r = random.randint(10000,99999)
    #use file manager to save the pirate dict into our pirate database
    f.writenewobject(r,d)
    win.destroy()
def selectImg():
    global win, imgLabel
    win.filename = filedialog.askopenfilename()
    basename = os.path.basename(win.filename)
    imgLabel.config(text = basename)
    
myfont="Arial 14 bold"
def loadwindow(root):
    global nBox, sBox, win, optionstring, imgLabel
    win = root
    root.geometry("500x400+900+50")
    root.title("Add a Pirate!")

    #generating...
    title = Label(root, text="New Pirate", font="Arial 20 bold")
    nameLabel =Label(root, text="Name", font=myfont)
    shipLabel =Label(root, text="Ship", font=myfont)
    fictLabel =Label(root, text="Fictional", font=myfont)
    
    nBox= Entry(root, font=myfont)
    sBox= Entry(root, font=myfont)
    btn= Button(root, text ="Save", font="Arial 20 bold", bg="#eeddff", command = addnew)

    #dropdown...
    optionstring= StringVar(root)
    optionstring.set("true")
    fictdrop = OptionMenu(root, optionstring, "true", "false")
    fictdrop.config(font=myfont)
    fictdrop.nametowidget(fictdrop.menuname).config(font=myfont)

    #select image
    pictButton = Button(root, text ="Picture", font="Arial 20 bold", bg="#eeddff", command = selectImg)
    imgLabel = Label(root, font = myfont)

    #adding...
    title.grid(row=0,column=0,columnspan=2)
    nameLabel.grid(row=1,column=0)
    shipLabel.grid(row=2,column=0)
    fictLabel.grid(row=3,column=0)
    nBox.grid(row=1, column=1)
    sBox.grid(row=2, column=1)
    pictButton.grid(row=4, column=0)
    btn.grid(row=5,column=5, columnspan=2, sticky = "E")
    fictdrop.grid(row=3,column=1, sticky="W")
    imgLabel.grid(row = 4, column = 1)
    
    root.mainloop()

