#الاسم : محمد علي محمد الدسوقي قزامل
#سكشن 4
from tkinter import *
root = Tk()
root.geometry("500x600")
root.title("Task")  
def setLabel():
    name = txt.get("1.0",'end') 
    lbl['text'] = name

btn = Button(root,text="Click Here",width=20,height=3,bg="blue",fg="white",font='22',command=setLabel)
btn.pack(side=BOTTOM,padx=15,pady=15)
txt = Text(root,height=10,width=30,fg="black",bg="white",font='22')
lbl = Label(root,width=20,font='22',bg="white",fg="black")
txt.pack()
lbl.pack()
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()