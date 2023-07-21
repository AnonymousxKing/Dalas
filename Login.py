from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import subprocess
#Creating Window Screen
window=Tk()
window.title("WELCOME")
window.geometry("500x300")
window.configure(bg="black")
window.configure(padx=20,pady=20)
window.resizable(False,False)
#Adding conditions
def Done():
  if usrt.get()==str.lower("Hussnain") and pswt.get()==str("0000"):
   messagebox.showinfo(title="Acces Granted",message="You Are Loged in,Thanks")
   usrt.delete(0,END)
   pswt.delete(0,END)
   window.destroy()
   print("A User is Detected ")
   import Data
  else:
    messagebox.showerror(title="Acces Denied",message="Please Enter The Corect UserName&Password")
#Defining Exit Fun
def Exit():
  window.destroy()
#Defining NextLine
def NextLine():
  return
#Adding Text Field
log=Label(window,text="LOG IN",font=("Impact",48),fg="purple",background="black")
log.grid(row=2,column=3)
#User Name Field 
usr=Label(window,text="UserName:",font=("Impact",18),fg="purple",background="black" )
usr.grid(row=5,column=2)
#creating text field
usrt=Entry(window,width=20,font=("Arial",16),fg="Black",background="White" )
usrt.grid(row=5,column=3)
#Password Label
psw=Label(window,text="Password: ",font=("Impact",18),fg="Purple",background="black",pady=20 )
psw.grid(row=6,column=2)
#creating text field
pswt=Entry(window,width=20,font=("Arial",16),fg="Black",background="White" )
pswt.grid(row=6,column=3)
#Creating Button
Bt=Button(window,text=" Log In ",command=Done)
Bt.grid(row=7,column=3)
#Key Binding aka Keyboard Commanding
window.bind('<Alt-KeyPress-F4>', lambda event:Exit())
window.bind("<Return>", lambda event:Done())
window.mainloop()
