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



def open_popup():
	 
	#while password != 'Forensic1':
		
	def printvalue():
		password=entry.get()
		Label(pop, text=f'                                                      ', font=('Mistral 10 bold'))
		Label(pop, text=f'Password={password}', font=('Mistral 10 bold')).place(x=50,y=40)
		entry.delete(0, END)

	Lable(pop, text= "WRONG PASSWORD", font=('Mistral 10 bold')).place(x=50,y=60)
	top.attributes('-fullscreen', False)
	top.geometry("2000x2000") 
	pop= Toplevel(top)
	pop.geometry("750x250")
	pop.title("Enter Password TO Exit")
	top.attributes('-fullscreen', True) 
	B=Button(pop,text="CANCEL", command=pop.destroy)
	B.place(x=200,y=200)
	count=0
	B=Button(pop,text="Enter Password", command=printvalue).place(x=300,y=200)
	Label(pop,text= "Please Enter Password", font=('Mistral 10 bold')).place(x=150,y=100)
	entry = Entry(pop, show="*", width=20)
	entry.pack()
	pop.attributes('-fullscreen', True)     
	top.attributes('-fullscreen', True)
	count +=1
	 #else:    
		#command=quit

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
  p=subprocess.Popen("idevice_id", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0] 
  p=p.split()[0].decode("utf-8")
  msg=messagebox.showinfo("iPhone Forensics", "Please Ensure iPhone is on and lead pluged in")
  msg=messagebox.showinfo("iPhone Forensics USB ID", (p))

  
 
  v1="idevicebackup2 -u "
  v2=" backup --full /home/kali/CaseData"
  iD=v1+p+v2
  command=iD
  msg=messagebox.showinfo("iD Value","iD="+(iD))
  top.iconify()
  subprocess.call(command, shell=True)
  
  
  # q=subprocess.Popen((iD), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]  
  top.deiconify()

 # while (q) != "Backup Successful.":
 #     Label(newWindow, text=(q))
  msg=messagebox.showinfo("iPhone Forensics Back Up", "Backup Complete of "+(p)+"& stored in /home/kalie/CaseData")


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

