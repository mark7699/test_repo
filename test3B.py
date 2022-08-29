#!/usr/bin/env python3
import subprocess
import tkinter as tk
from tkinter import *

from tkinter import messagebox
import os
import subprocess

try:

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
        pop=Toplevel(top)
        pop.attributes('-fullscreen', True)

        def _shutdown():
            command = "poweroff"
            subprocess.call(command, shell=True)

        B4=Button(pop, text="POWER\n OFF", bg="red", height=3, width=6, command=_shutdown)
        B4.place(x=350, y=400)
        B=Button(pop, text="CANCEL", command=pop.destroy)
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

    def Unlock():
        top.option_add('*Font', 'Arial 10')
        top.option_add('*Dialog.msg.wrapLength', '7.5i')
        top.geometry("1000x1000")
        msg = messagebox.showinfo(" Unlock iPhone", "                                    Connect iPhone with USB and place in DFU mode.\n The list of supported devices includes:\n iPhone 5s, iPhone 6, iPhone SE, iPhone 6s, iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, iPhone X, Most iPads based on similar SoC, Apple TV HD (ATV4), Apple V 4K, Apple Watch series 1, 2 and 3\n \nTo enter DFU mode:\n\nA10 devices (iPhone 7 and iPhone 7 Plus, iPad 2018, iPod touch 7)\nConnect the device using a USB cable., Hold down both the Side button and Volume Down button., After 8 seconds, release the Side button while continuing to hold down the Volume Down button., If the Apple logo appears, the Side button was held down for too long., Nothing will be displayed on the screen when in DFU mode., If your device shows a screen telling you to connect the device to iTunes, retry these steps.\n \n A11 and newer devices (iPhone 8 and above, iPad Pro 2018, iPad Air 2019, iPad Mini 2019):\nConnect the device using a USB cable., Quick-press the Volume Up button, Quick-press the Volume Down button, Hold down the Side button until the screen goes black, then hold down both the Side button and Volume Down button., After 5 seconds, release the Side button while continuing to hold down the Volume Down button., If the Apple logo appears, the Side button was held down for too long., Nothing will be displayed on the screen when the device is in DFU mode.\n \n Apple Watch:\n Connect to computer via iBUS adapter and lightning cable., 1. Hold crown and power button (bottom right), Wait for the screen to go black, After 3 seconds of black, let go of the power button but continue to hold the crown, After about 5 seconds your watch will be in DFU mode")
        top.iconify()
        os.system('cd')
        command="cd /home/kali/Desktop; sudo ./checkra1n"
        subprocess.call(command, shell=True)
        # command = "sudo ./home/kali/Desktop/checkra1n"
        #subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #subprocess.run(command, shell=True)
        top.deiconify()


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
    B=Button(top,text="iPhone\nBackup",bg="white", height=3, width=6, command=iPhone)
    B.place(x=210,y=150)
    B=Button(top,text="RF\nSCANNER",bg="yellow", height=3, width=6, command=opengqrx)
    B.place(x=290,y=150)
    B=Button(top,text="Unlock\n iPhone",bg="yellow", height=3, width=6, command=Unlock)
    B.place(x=210,y=220)
    B=Button(top,text="ANDRIOD",bg="red", height=3, width=6, command=andriod)
    B.place(x=130,y=220)
    B=Button(top,text="READ\nCARD",bg="yellow", height=3, width=6, command=readcard)
    B.place(x=50,y=220)
    B=Button(top,text="EXIT", command=open_popup)
    B.place(x=400,y=400)
    top.attributes('-fullscreen', True)
    top.mainloop()

except Exception as e:
    with open("errorfile", "w") as f:
        f.write(e)