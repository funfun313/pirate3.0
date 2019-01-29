from tkinter import *
import firebasemanager

window1 = Tk()
def dofilter(e):
    filt = searchbox.get()
    listbox.delete(0, "end") #this is the listbox

    for pirate in d:
        if filt.lower() in d[pirate]["name"].lower():
            listbox.insert(END, d[pirate]["name"])
#frame1
frame1= Frame(window1)
title =Label(frame1,text="Pirate Database", font="Arial 20")
title.pack()

#frame2
frame2= Frame(window1)
searchhere =Label(frame2,text= "Search Here:", font="Arial 15")
searchbox = Entry(frame2, font="Arial 20")
searchbox.bind("<KeyRelease>", dofilter)
searchbox.grid(row=0, column=1)
searchhere.grid(row=0,column=0)
#frame3
frame3= Frame(window1)
name =Label(frame3, text="Name", font="Arial 20")
name.grid(row=0,column=1)
arrow1 =Button(frame3, text="<", font="Arial 20")
arrow1.grid(row=1,column=0)
pic =Label(frame3, text="picture", font="Arial 16", padx=100)
pic.grid(row=1,column=1)
arrow2 =Button(frame3, text=">", font="Arial 20")
arrow2.grid(row=1,column=2)
ship =Label(frame3, text="Ship", font="Arial 16")
ship.grid(row=2,column=1)
fict =Label(frame3, text="Fictional", font="Arial 16")
fict.grid(row=3,column=1)
#frame4
frame4= Frame(window1)
listbox = Listbox(frame4, font="Arial 20")
listbox.grid(row=0,column=0, columnspan=2)
    #retrieve pirates from dictionarys
fm = firebasemanager.FirebaseManager()
d = fm.getallpirates()
for item in d:
    listbox.insert(END, d[item]["name"])
new =Button(frame4, text="New", font="Arial 20")
new.grid(row=1,column=0)
quitme =Button(frame4, text="Quit", font="Arial 20")
quitme.grid(row=1,column=1)
    
#grid the frames into the window
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
