
#importing required Library----

import pyperclip
import pyshorteners
from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.geometry('1000x500')
root.title("URL-Shortener")
root.configure(bg="#49A")
root.bg=ImageTk.PhotoImage(file="images/frontpage.jpg")
bg=Label(root, image= root.bg).place(x=0,y=0,relwidth=1,relheight=1)

url=StringVar()
url_add=StringVar()

def urlshortener():
    url_address=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(url_address)
    url_add.set(url_short)

def copyurl():
    url_short=url_add.get()
    pyperclip.copy(url_short)

Label(root,text="My URL Shortener",height=0, width=15,font=("times new roman",20,"bold")).pack(pady=20)
Entry(root,textvariable=url).pack(pady=20)
Button(root,text="Generate Short URL",height=0, width=15,font=("times new roman",20,"bold"),command=urlshortener).pack(pady=20)
Entry(root,textvariable=url_add).pack(pady=20)
Button(root,text="Copy URL",command=copyurl).pack(pady=20)

root.mainloop() 
