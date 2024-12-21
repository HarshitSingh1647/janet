from tkinter import *
from settings import *
import sys
root2=Tk()
root2.title("Settings")
root=Frame(root2,bg="#232323",height=300,width=500)
root.grid(row=1,column=2,padx=25,pady=25,rowspan=9,columnspan=10)
root.grid_propagate(0)

bg6="#232323"
fg1="white"

yobg="#023e8a"
root2.configure(bg="#121212")
root2.protocol("EM_DELETE _WINDOW",sys.exit)
malef=IntVar()
femalef=IntVar()


def fu1():
    namecan.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=5)
    gencan.grid(row=1, column=3, padx=18, pady=5, sticky="w")
    thcan.grid_forget()
    fontcan.grid_forget()
    bcan.grid_forget()
    lcan.grid_forget()

def fu2():
    bcan.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=5)
    gencan.grid_forget()
    namecan.grid_forget()
    thcan.grid_forget()
    fontcan.grid_forget()

    lcan.grid_forget()

def fu3():
    thcan.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=5)
    gencan.grid_forget()
    namecan.grid_forget()
    lcan.grid_forget()
    fontcan.grid_forget()
    bcan.grid_forget()
def fu4():
    lcan.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=5)
    gencan.grid_forget()
    thcan.grid_forget()
    bcan.grid_forget()
    fontcan.grid_forget()
    namecan.grid_forget()


def chatheme(thc):


    if thc == "dark":
        dkd.grid(row=1, column=2, pady=10, padx=10)
        dkl.grid_forget()
        with open("tb.py","w") as t:
            t.write(f"theme=\"{thc}\"")
    elif thc == "light":
        dkl.grid(row=1, column=2, pady=10, padx=10)
        dkd.grid_forget()
    with open("tb.py", "w") as t:
        t.write(f"theme=\"{thc}\"")
def hff():
    dark.configure(bg=yobg,fg="white")
    light.configure(bg=bg6,fg=fg1)
    with open("lb.py","w") as l:
        l.write("language=\"hindi\"")
def eff():
    dark.configure(bg=bg6,fg=fg1)
    light.configure(bg=yobg,fg="white")
    with open("lb.py","w") as l:
        l.write("language=\"english\"")

def qbf():
    qb.configure(bg=yobg,fg="white")
    db.configure(bg=bg6,fg=fg1)
    with open("bb.py","w") as l:
        l.write("browser=\"qb\"")
def dff():
    qb.configure(bg=bg6,fg=fg1)
    db.configure(bg=yobg,fg="white")
    with open("bb.py","w") as l:
        l.write("browser=\"local\"")
def femalef(self):
    male.deselect()
    with open("genb.py","w") as l:
        l.write("gender=\"female\"")
def malef(self):
    female.deselect()
    with open("genb.py","w") as l:
        l.write("gender=\"male\"")


namecan=Canvas(root,bg=bg6,highlightthickness=0)
namecan.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=5)
name_label=Button(root2,text="User details",font=("Helvetica 18 bold"),fg="white",bg="#121212",border=0,highlightthickness=0,command=fu1)
name_label.grid(row=1,column=1,padx=10,pady=15,sticky="w")

nameentry=Entry(namecan,bg="light grey",border=0,fg="black",font=("Helvetica",15))
nameentry.grid(row=2,column=1,padx=10,pady=10)
nameentry.insert(0,username)
gencan=Canvas(root,bg=bg6,highlightthickness=0)
gencan.grid(row=1,column=3,padx=18,pady=5,sticky="w")

genderl=Label(gencan,text="User gender",font=("Helvetica 15 bold"),bg=bg6,border=0,highlightthickness=0,fg=fg1)
genderl.grid(row=1,column=1,pady=5,padx=5,sticky="w",columnspan=2)



male=Checkbutton(gencan,text="Male",font=("Helvetica",10),bg=bg6,border=0,highlightthickness=0,onvalue=1,offvalue=0,variable=malef,selectcolor=bg6,fg=fg1)
male.grid(row=2,column=1,pady=15,padx=10,sticky="w")
male.bind("<Button-1>",malef)
female=Checkbutton(gencan,text="Female",font=("Helvetica",10),bg=bg6,border=0,highlightthickness=0,onvalue=1,offvalue=0,variable=femalef,selectcolor=bg6,fg=fg1)
female.bind("<Button-1>",femalef)
female.grid(row=2,column=2,pady=15,padx=10,sticky="w")

if usergender=="male":
    male.select()
    female.deselect()
elif usergender=="female":
    female.select()
    male.deselect()
bcan=Canvas(root,bg=bg6,border=0,highlightthickness=0)

bl=Button(root2,text="Default browser",font=("Helvetica 18    bold"),bg="#121212",fg="white",border=0,highlightthickness=0,command=fu2)
bl.grid(row=2,column=1,padx=10,sticky="w")


qb=Button(bcan,border=0,bg=bg6,text="Qbrowser",font=("Helvetica 15 italic"),fg=fg1,command=qbf)
qb.grid(row=2,column=1,sticky="w",padx=5,pady=5)


db=Button(bcan,text="Default system browser",font=("Helvetica 15"),fg=fg1,bg=bg6,border=0,command=dff)
db.grid(row=2,column=2,sticky="w",padx=5,pady=5)
if browser=="qb":
    qb.configure(bg=yobg,fg="white")
    db.configure(bg=bg6)
if browser=="local":
    qb.configure(bg=bg6)
    db.configure(bg=yobg,fg="white")

thcan=Canvas(root,bg=bg6,border=0,highlightthickness=0)

tjl=Button(root2,text="Language",font=("Helvetica 18 bold"),bg="#121212",fg="white",border=0,command=fu3)
tjl.grid(row=3,column=1,sticky="w",padx=10)


dark=Button(thcan,text="Hindi",font=("Helvetica 13   italic"),bg=bg6,fg=fg1,border=0,command=hff)
dark.grid(row=3,column=1,sticky="w",padx=5,pady=5)


light=Button(thcan,text="English",font=("Helvetica 13   italic"),bg=bg6,fg=fg1,border=0,command=eff)
light.grid(row=3,column=2,sticky="w",padx=5,pady=5)


if language=="hi-IN":
    light.configure(bg=bg6,fg=fg1)
    dark.configure(bg=yobg,fg="white")
elif language=="en-IN":
    dark.configure(bg=bg6, fg=fg1)
    light.configure(bg=yobg, fg=fg1)

lcan=Canvas(root,bg=bg6,border=0,highlightthickness=0)

ll=Button(root2,text="Theme",font=("Helvetica 18    bold"),bg="#121212",fg="white",border=0,command=fu4)
ll.grid(row=4,column=1,sticky="w",padx=10)

dkil=PhotoImage(file="lib/off.png")
dkid=PhotoImage(file="lib/on.png")
dkd=Button(lcan,text="Dark theme",image=dkid,compound="right",bg=bg6,fg=fg1,border=0,command=lambda :chatheme("light"))


dkl=Button(lcan,text="Dark theme",image=dkil,compound="right",bg=bg6,fg=fg1,border=0,command=lambda :chatheme("dark"))
if theme=="dark":
    dkd.grid(row=1,column=2,pady=10,padx=10)
elif theme=="light":
    dkl.grid(row=1,column=2,pady=10,padx=10)
fontcan=Canvas(root,bg=bg6,border=0,highlightthickness=0)


fl=Button(fontcan,text="Font style",font=("Helvetica 15 bold"),bg=bg6,fg=fg1,border=0)
fl.grid(row=5,column=1,sticky="w",padx=10)
fle=Entry(fontcan,bg="#2596be",border=0,fg="white",font=("Helvetica",15))
fle.grid(row=1,column=2,sticky="w",padx=15,pady=10)
fle.insert(0,font)

finalbtn=Button(root2,text="Apply",font=("Helvetica 13"),bg="#023e8a",fg="white",border=0)
finalbtn.grid(row=10,column=11,ipadx=5,ipady=3,pady=3,sticky="n")
cabtn=Button(root2,text="Cancle",font=("Helvetica 13"),bg="#252525",fg="white",border=0,command=sys.exit)
cabtn.grid(row=10,column=12,ipadx=3,ipady=3,pady=5,sticky="nw")
root.mainloop()
