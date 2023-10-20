import tkinter as tk
from tkinter import *
from tkinter import ttk       
 
window=tk.Tk()
window.title("TEST")
dengei=tk.IntVar()
dengei2=tk.StringVar()
def display():
    fff=dengei.get()
    dengei2.set(f"сіз (dengei2) деңгей таңдаңыз")
    if fff==1:
        print("ote onai")
    elif fff==2:
        print("onai")
    elif fff==3:
        print("orta")
    elif fff==4:
        print("qiyn")
    elif fff==5:
        print("ote qiyn")    

label=tk.Ladel(window,text="деңгей таңда").pack()
radio=ttk.Radiobutton(window,text="өте оңай",variable=dengei,value=1,command=display).pack()
radio=ttk.Radiobutton(window,text="оңай",variable=dengei,value=1,command=display).pack()
radio=ttk.Radiobutton(window,text="орта",variable=dengei,value=1,command=display).pack()
radio=ttk.Radiobutton(window,text="қиын",variable=dengei,value=1,command=display).pack()
radio=ttk.Radiobutton(window,text="өте қиын",variable=dengei,value=1,command=display).pack()
label=ttk.Label(window,textvariable=dengei2).pack()
window.mainloop()