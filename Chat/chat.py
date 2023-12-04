from tkinter import *
import datetime

root = Tk()

def envoie():
    envoie = "moi" + e.get()
    txt.insert(END,"\n" +envoie)


txt = Text(root)
txt.grid(row = 0, column = 0,columnspan=10)
e = Entry(root, width=100)
e.grid(row=1,column=0)
envoyer =  Button(root, text="Envoyer" ,command=envoie).grid(row=1,column=1)
 
root.title("My chat [...]") # c'est le titre de la fenetre
root.mainloop()
