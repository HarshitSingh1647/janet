from tkinter import *
import matplotlib.pyplot as mat


index = 0
charttype=[]
chartnamel=[]
y=[]
values=[]

name = []
root=Tk()




def getChartType():
    chartnamel.insert(0,chartname.get())
    chartname["state"] = "disabled"
    okw["state"] = "disabled"
    charttype.insert(0,f"{whichChart.get()}")
    whichChart["state"] = "disabled"
    setwin()

def final():
    if charttype[0]=="bar chart" or charttype[0]=="bar" or charttype[0]=="Bar" or charttype[0] == "Bar chart":
        mat.bar(name,values)
        mat.title(chartnamel[0])
        mat.show()
    if charttype[0]=="pie" or charttype[0]=="pie chart" or charttype[0]=="Pie" or charttype[0] == "Pie chart":
        mat.pie(values,labels=name)
        mat.title(chartnamel[0])
        mat.show()
    if charttype[0]=="scatter chart" or charttype[0]=="scatter" or charttype[0]=="Scatter chart" or charttype[0] == "Scatter":
        mat.scatter(values,y)
        mat.title(chartnamel[0])
        mat.show()
def new(event):

    global index
    content = entry.get()
    entry.delete(first=0,last=100)
    if charttype[0]=="scatter chart" or charttype[0]=="scatter" or charttype[0]=="Scatter chart" or charttype[0] == "Scatter":
        ycon=yv.get()
        yv.delete(first=0,last=200)
    nam=totalmarks.get()
    totalmarks.delete(first=0,last=200)
    if charttype[0]=="scatter chart" or charttype[0]=="scatter" or charttype[0]=="Scatter chart" or charttype[0] == "Scatter":
        y.insert(index,float(ycon))
        values.insert(index,float(content))

    else:
        name.insert(index,nam)
        values.insert(index,float(content))
    index=index+1


def setwin():

    totalmarkslabel.pack()
    totalmarks.pack()
    label.pack()
    entry.pack()
    if charttype[0]=="scatter chart" or charttype[0]=="scatter" or charttype[0]=="Scatter chart" or charttype[0] == "Scatter":
        label.configure(text="enter x value",font=("Calibri",17))
        root.update()
        yvl.pack()
        yv.pack()
    ok.pack(side="bottom")

root.title("Chart Maker")

itsLabel=Label(root,text="Type of chart",font=("Calibri",20))
options=Label(root,text="options - bar , pie , scatter",font=("Calibri",12))
whichChart=Entry(root,font=("Calibri",23))
okw=Button(root,text="Ok",command=getChartType)


totalmarkslabel=Label(root,text="name of the criteria",font=("Calibri",17))

totalmarks=Entry(root,font=("Calibri",20))

label=Label(root,text=f"enter points of criteria",font=("Calibri",15))

entry = Entry(root,font=("Calibri",15))



root.bind("<Return>",new)
ok=Button(root,text=" Okay ",command=final)

yv=Entry(root,font=("Calibri",15))
yvl=Label(root,text=" Enter y value",font=("Calibri",17))

itsLabel.pack(side="top")
options.pack(side="top")
whichChart.pack(side="top")
chartnamela=Label(root,text="enter chart name")
chartnamela.pack(side="top")
chartname=Entry(root,font=("Calibri",15))
chartname.pack(side="top")
okw.pack(side="top")

root.mainloop()


