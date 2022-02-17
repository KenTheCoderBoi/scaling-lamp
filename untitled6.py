from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("among job")
label=Label(root,text="enter name")
label.place(relx=0.2,rely=0.05,anchor=CENTER)
entry=Entry(root)
entry.place(relx=0.3,rely=0.05,anchor=CENTER)
label1=Label(root,text="Chemist")
label1.place(relx=0.3,rely=0.1,anchor=CENTER)
label2=Label(root,text="explosive")
label2.place(relx=0.3,rely=0.3,anchor=CENTER)
label3=Label(root,text="knietic")
label3.place(relx=0.3,rely=0.5,anchor=CENTER)
class parent():
    def ChemicalEngineer(name):
        label1["text"]=name+" has been assigned to candice factory"
    def ExplosiveEngineer(name):
        label2["text"]=name+" has been assigned to missle factory"
    def KnieticEngineer(name):
        label3["text"]=name+" has been assigned to knietic lab"
class child(parent):
    def chem():
        parent.ChemicalEngineer(entry.get())
    def exp():
        parent.ExplosiveEngineer(entry.get())
    def kni():
        parent.KnieticEngineer(entry.get())
button1=Button(root,text="generate",command=child.chem)
button1.place(relx=0.2,rely=0.1,anchor=CENTER)
button2=Button(root,text="generate",command=child.exp)
button2.place(relx=0.2,rely=0.3,anchor=CENTER)
button3=Button(root,text="generate",command=child.kni)
button3.place(relx=0.2,rely=0.5,anchor=CENTER)
root.mainloop()