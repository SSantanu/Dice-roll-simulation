from tkinter import *
from random import randrange
root=Tk()
root.geometry("600x600")
root.configure(background='white')
image1=PhotoImage(file="dice\\1.png")
image2=PhotoImage(file="dice\\2.png")
image3=PhotoImage(file="dice\\3.png")
image4=PhotoImage(file="dice\\4.png")
image5=PhotoImage(file="dice\\5.png")
image6=PhotoImage(file="dice\\6.png")
image7=PhotoImage(file="dice\\roll.png")
def task():
    for i in range(10):
        lbl.config(image=list[randrange(0,6)])
        lbl.update()
        lbl.after(100)
    num=randrange(0,6)
    lbl.config(image=list[num])
list=[image1,image2,image3,image4,image5,image6]
frame=Frame(root,height=200,width=200,bg='black')
lbl=Label(frame,image=image6,bg='white')
lbl.place(x=0,y=0)
frame.place(x=200,y=90)
bt=Button(root,image=image7,command=task,bd=0,bg='white')
bt.place(x=210,y=350)
root.mainloop()