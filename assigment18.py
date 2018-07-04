#create dict with name and no.
#in same file create a fx. to insert items into dict

from tkinter  import *
top=Tk()
def display():
    k = d.get(ACTIVE)
    v = dict[k]
    label1.config(text=k)
    label2.config(text=v)
s=Scrollbar(top)
s.pack(side=RIGHT,fill=Y)
d=Listbox(top,yscrollcommand=s.set)
d.pack()
dict={'rishabh':'76760','serv':'844656','rohit':'758389'}



for k in dict.keys():
    d.insert(END,k)
s.config(command=d.yview)

b=Button(top,text="click",width=30,bg="red",fg="brown",command=display)
label1=Label(top,text="name",width=30)
label1.pack()
label2=Label(top,text="contact",width=30)
label2.pack()


def show():
    k=(e1.get())
    v=(e2.get())
    dict[k]=v
    print(dict)
    d.insert(END,k)
e1 = Entry(top,width=30,text="name")
e1.pack()
e2 = Entry(top,width=30,text="contact")
e2.pack()
b1 = Button(top, text= "Insert", command=show)
b1.pack()
b.pack()


top.mainloop()
