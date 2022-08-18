#!/usr/bin/env python3
import subprocess
import tkinter as tk
from tkinter import *

from tkinter import messagebox 

top=Tk()
Label_middle=tk.Label(top,text='ENGINEERING & FORENSIC SERVICES', fg="blue", font=("Arial", 30))
Label_middle.place(relx=0.5,rely=0.05,anchor='n')
Label_middle=tk.Label(top,text='(FORENSIC SYSTEM EFS 1)', fg="blue", font=("Arial", 20))
Label_middle.place(relx=0.5,rely=0.14,anchor='n')
logo=PhotoImage(file="/home/kali/Pictures/Atom efs 1v.PNG")
label=tk.Label(top, image=logo)
label.place(relx=0.5,rely=0.2,anchor='n')
top.attributes('-fullscreen', True)

global count

def open_popup():
    global count, errorlabel
    #while password != 'Forensic1':
    pop= Toplevel(top)
    pop.attributes('-fullscreen', True)
    B4= Button(pop, text="POWER\n OFF", bg="red", height=3, width=6, command="sudo poweroff")
    B4.place(x=350, y=400)
    B = Button(pop, text="CANCEL", command=pop.destroy)
    B.place(x=200, y=200)
    count=0
    errorlabel = Label(pop, text="You have 3 attempts.", font=('Mistral 10 bold'))
    errorlabel.place(x=300, y=45)

    # errorlabel.update()
    def printvalue():
        global count, errorlabel
        password=entry.get()

        if password=="Forensic1":
            quit()
        else:
            count+=1
            if count==3:
                pop.destroy()
            # errorlabel.text=str(count) + "WRONG PASSWORD"
            countleft = 3-count
            errorlabel.destroy()
            errorlabel = Label(pop, text= "You have only " + str(countleft) + " attempt(s) left.", font=('Mistral 10 bold'))
            errorlabel.place(x=300, y=45)
        entry.delete(0, END)

    B2 = Button(pop, text="Enter Password", command=printvalue).place(x=400, y=200)
    Label(pop, text="Please enter password to quit the EFS1 console", font=('Mistral 10 bold')).place(x=150, y=100)
    entry = Entry(pop, show="*", width=20)
    entry.place(x=150, y=150)
    # entry.pack()





def readcard():

    command="cardpeek"    
    subprocess.call(command, shell=True)


def andriod():
    command="cd env/bin ; python3 andriller-gui.py"    
    subprocess.call(command, shell=True)


def opengqrx():
    command="gqrx"
    subprocess.call(command, shell=True)


def helloCallBack():
  command="./can"
  subprocess.call(command, shell=True)

def run_guymager():
  command="sudo guymager"
  subprocess.call(command, shell=True) 

def iPhone():
    global p
    msg=messagebox.showinfo("iPhone Forensics", "Please Ensure iPhone is on, lead plugged in and you select TRUST on the iPhone Screen")
    p=subprocess.Popen("idevice_id -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    p=p.split()[0].decode("utf-8")
    msg=messagebox.showinfo("iPhone Forensics USB ID", (p))

    v1="idevicebackup2 -u "
    v2=" backup --full /home/kali/CaseData"
    iD=v1+p+v2
    msg=messagebox.showinfo("iD Value","iD="+(iD))
    top.iconify()
    command=iD
    subprocess.call(command, shell=True)
    msg=messagebox.showinfo("iPhone Forensics Back Up", "Backup Complete of "+(p)+"& stored at /home/kali/CaseData")

def iPhon_Parser():
    global p2
  #ileapp python3 ileapp.py -t itunes -o /home/kali/CaseData -i /home/kali/CaseData/00008101-000910441E7A001E

    command="cd /Downloads/iLEAPP-master"
    ileapp1="python3 ileapp.py -t itunes -o /home/kali/CaseData -i /home/kali/CaseData/"
    iPhoneReport=ileapp1+p
    subprocess.call(command, shell=True)
    top.deiconify()
    p2 = subprocess.Popen(iPhoneReport, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    p2 =p2.split()[0].decode("utf-8")
    subprocess.call(command, shell=True)
    top.deiconify()
    msg = messagebox.showinfo("REPORT COMPLETE", "HTML report completed of" + (p) + "& stored as"+p2)

B=Button(top,text="KAYAK\n(CAN)",fg="white",bg="blue", height=3, width=6, command=helloCallBack)
B.place(x=50,y=150)
B=Button(top,text="FORENSIC\n COPYING",bg="green", height=3, width=6, command=run_guymager)
B.place(x=130,y=150)
B=Button(top,text="iPhone",bg="white", height=3, width=6, command=iPhone)
B.place(x=210,y=150)
B=Button(top,text="RF\nSCANNER",bg="yellow", height=3, width=6, command=opengqrx)
B.place(x=290,y=150)
B=Button(top,text="ANDRIOD",bg="red", height=3, width=6, command=andriod)
B.place(x=210,y=220)
B=Button(top,text="READ\nCARD",bg="yellow", height=3, width=6, command=readcard)
B.place(x=50,y=220)
B=Button(top,text="EXIT", command=open_popup)
B.place(x=400,y=400)
top.attributes('-fullscreen', True)
top.mainloop()

