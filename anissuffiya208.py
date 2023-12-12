from tkinter import*
root=Tk()
root.geometry("1000x500")
root.title("Waffle Bite")
root.resizable(False,False)

def Reset():
    entry_Kaya.delete(0,END)
    entry_Nutella.delete(0,END)
    entry_Hazelnut.delete(0,END)
    entry_Butter.delete(0,END)
    entry_Chocolate.delete(0,END)
    entry_Mix.delete(0,END)
    entry_Tin.delete(0,END)

def Total():
    try:a1=int(Kaya.get())
    except:a1=0

    try:a2=int(Nutella.get())
    except:a2=0

    try:a3=int(Hazelnut.get())
    except:a3=0

    try:a4=int(Butter.get())
    except:a4=0

    try:a5=int(Chocolate.get())
    except:a5=0

    try:a6=int(Mix.get())
    except:a6=0

    try:a7=int(Tin.get())
    except:a7=0

    #define cost of each item per quantity 
    c1=4*a1
    c2=7*a2
    c3=5*a3
    c4=3*a4
    c5=6*a5
    c6=8*a6
    c7=2*a7

    lbl_total=Label(f2,font=("rockwell",20,"bold"),text="Total",width=16,fg="pink3",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("times new roman",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgrey")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="RM",str("%.2f" %totalcost)
    Total_bill.set(string_bill)


Label(text="W A F F L E       B I T E",bg="pink4",fg="white",font=("cooper black",30),width="310",height="2").pack()

#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="darkgreen",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Bodoni mt black",40,"bold"),fg="black",bg="lightgreen").place(x=65,y=0)

Label (f,font=("Rockwell",15,"bold"),text="Kaya...................... RM4.00",fg="black",bg="lightgreen").place(x=5,y=95)
Label (f,font=("Rockwell",15,"bold"),text="Nutella................... RM7.00",fg="black",bg="lightgreen").place(x=5,y=125)
Label (f,font=("Rockwell",15,"bold"),text="Hazelnut ................ RM5.00",fg="black",bg="lightgreen").place(x=5,y=155)
Label (f,font=("Rockwell",15,"bold"),text="Butter .................... RM3.00",fg="black",bg="lightgreen").place(x=5,y=185)
Label (f,font=("Rockwell",15,"bold"),text="Chocolate............... RM6.00",fg="black",bg="lightgreen").place(x=5,y=215)
Label (f,font=("Rockwell",15,"bold"),text="Mix ....................... RM8.00",fg="black",bg="lightgreen").place(x=5,y=245)
Label (f,font=("Rockwell",15,"bold"),text="Air Tin................... RM2.00",fg="black",bg="lightgreen").place(x=5,y=275)


#BILL
f2=Frame(root,bg="pink3",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("Lucida Fax",20),bg="pink3")
Bill.place(x=120,y=10)

#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Kaya=StringVar() 
Nutella=StringVar() 
Hazelnut=StringVar() 
Butter=StringVar() 
Chocolate=StringVar() 
Mix=StringVar() 
Tin=StringVar() 
Total_bill=StringVar() 

#Label
lbl_Kaya=Label(f1,font=("Bell MT",20,"bold"),text="Waffle Kaya",width=12,fg="blue3")
lbl_Nutella=Label(f1,font=("Bell MT",20,"bold"),text="Waffle Nutella",width=12,fg="blue3")
lbl_Hazelnut=Label(f1,font=("Bell MT",20,"bold"),text="Waffle Hazelnut",width=12,fg="blue3")
lbl_Butter=Label(f1,font=("Bell MT",20,"bold"),text="Waffle Butter",width=12,fg="blue3")
lbl_Chocolate=Label(f1,font=("Bell MT",20,"bold"),text="WaffleChocolate",width=12,fg="blue3")
lbl_Mix=Label(f1,font=("Bell MT",20,"bold"),text="Waffle Mix",width=12,fg="blue3")
lbl_Tin=Label(f1,font=("Bell MT",20,"bold"),text="Air Tin",width=12,fg="blue4")
lbl_Kaya.grid(row=1,column=0)
lbl_Nutella.grid(row=2,column=0)
lbl_Hazelnut.grid(row=3,column=0)
lbl_Butter.grid(row=4,column=0)
lbl_Chocolate.grid(row=5,column=0)
lbl_Mix.grid(row=6,column=0)
lbl_Tin.grid(row=7,column=0)

#Entry
entry_Kaya=Entry(f1,font=("times new roman",20,"bold"),textvariable=Kaya,bd=6,width=8,bg="pink")
entry_Nutella=Entry(f1,font=("times new roman",20,"bold"),textvariable=Nutella,bd=6,width=8,bg="pink")
entry_Hazelnut=Entry(f1,font=("times new roman",20,"bold"),textvariable=Hazelnut,bd=6,width=8,bg="pink")
entry_Butter=Entry(f1,font=("times new roman",20,"bold"),textvariable=Butter,bd=6,width=8,bg="pink")
entry_Chocolate=Entry(f1,font=("times new roman",20,"bold"),textvariable=Chocolate,bd=6,width=8,bg="pink")
entry_Mix=Entry(f1,font=("times new roman",20,"bold"),textvariable=Mix,bd=6,width=8,bg="pink") 
entry_Tin=Entry(f1,font=("times new roman",20,"bold"),textvariable=Tin,bd=6,width=8,bg="pink") 
entry_Kaya.grid(row=1,column=1)
entry_Nutella.grid(row=2,column=1)
entry_Hazelnut.grid(row=3,column=1)
entry_Butter.grid(row=4,column=1)
entry_Chocolate.grid(row=5,column=1)
entry_Mix.grid(row=6,column=1)
entry_Tin.grid(row=7,column=1) 

#buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("Cascadia Code",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("Cascadia Code",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
