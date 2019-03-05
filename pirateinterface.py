from tkinter import *
import firebasemanager
import newpirate
window2 = ""
def newpiratebutton():
    global window2
    window2 = Toplevel()
    newpirate.loadwindow(window2)
window1 = Tk()
def listdelete():
    index = int(listbox.curselection()[0])
    piratename = listbox.get(index)
    deletekey = ""
    for pirate in d:
        if d[pirate]["name"] == piratename:
            deletekey = pirate
    fm.deletepirate(deletekey)
    d.pop(deletekey)
    filt = searchbox.get()
    listbox.delete(0, "end") #this is the listbox

    for pirate in d:
        if filt.lower() in d[pirate]["name"].lower():
            listbox.insert(END, d[pirate]["name"])
    
def dofilter(e):
    filt = searchbox.get()
    listbox.delete(0, "end") #this is the listbox

    for pirate in d:
        if filt.lower() in d[pirate]["name"].lower():
            listbox.insert(END, d[pirate]["name"])
def onselect(e):
    w = e.widget
    try:
        index = int(w.curselection() [0])
        pirate = w.get(index)
        #print (pirate, " selected")
        for p in d:
            if d[p]["name"].lower() == pirate.lower():
               display(p)
    except:
        pass
                
def display(pirate_id):
    name.config(text =d[pirate_id]["name"])
    ship.config(text =d[pirate_id]["ship"])
    if d[pirate_id]["fictional"]== "true":
        fict.config(text = "Fictional")
    else:
        fict.config(text = "Not Fictional")
def scrollright():
    try:
        index = int(listbox.curselection()[0])
        listbox.selection_clear(index)
        if index == len(d)-1:
            update_listbox(0)
        else:
            update_listbox(index + 1)
    except:
        index = 0
        update_listbox(0)

def scrollleft():
    try:
        index = int(listbox.curselection()[0])
        listbox.selection_clear(index)
        if index == 0:
            update_listbox(listbox.size()-1)
        else:
            update_listbox(index - 1)
    except:
        update_listbox(listbox.size()-1)
        

def update_listbox(index):
    listbox.selection_set(index)
    piratename = listbox.get(index)
    for p in d:
         if d[p]["name"].lower() == piratename.lower():
               display(p)
    
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
arrow1 =Button(frame3, text="<", font="Arial 20", command = scrollleft)
arrow1.grid(row=1,column=0)
pic =Label(frame3, text="picture", font="Arial 16", padx=100)
pic.grid(row=1,column=1)
arrow2 =Button(frame3, text=">", font="Arial 20", command = scrollright)
arrow2.grid(row=1,column=2)
ship =Label(frame3, text="Ship", font="Arial 16")
ship.grid(row=2,column=1)
fict =Label(frame3, text="Fictional", font="Arial 16")
fict.grid(row=3,column=1)
#frame4
frame4= Frame(window1)
listbox = Listbox(frame4, font="Arial 20")
listbox.grid(row=0,column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", onselect)
    #retrieve pirates from dictionarys
fm = firebasemanager.FirebaseManager()
d = fm.getallpirates()
for item in d:
    listbox.insert(END, d[item]["name"])
new =Button(frame4, text="New", font="Arial 20", command = newpiratebutton)
new.grid(row=1,column=0)
deleteme =Button(frame4, text="Delete", font="Arial 20", command = listdelete)
deleteme.grid(row=1,column=1)
quitme =Button(frame4, text="Quit", font="Arial 20")
quitme.grid(row=1,column=2)
    
#grid the frames into the window
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
