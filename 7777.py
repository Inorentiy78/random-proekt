import tkinter as tk
from tkinter import *
from tkinter import ttk

window=tk.Tk()
window.title("TEST")
window.geometry=("1080x1080")
esep=StringVar()
a=0
def calculate():
    global a
    if esep.get()=="1":
        a=a+2
    elif esep.get()=="8":
        a=a+2
    elif esep.get()=="11":
        a=a+2
        label.config(text=a)
    elif esep.get()=="13":
        a=a+2
        label.config(text=a)
    elif esep.get()=="18":
        a=a+2
        label.config(text=a)
    elif esep.get()=="23":
        a=a+2
        label.config(text=a)
    elif esep.get()=="28":
        a=a+2
        label.config(text=a)
    elif esep.get()=="29":
        a=a+2
    else:
        label.config(text=a)
Label(window,text=a).pack()        

rad=IntVar()
label=tk.Label(window,text="1.Python-ды қалай іске қосамыз?")
label.pack()
rad=IntVar()
ttk.Radiobutton(window,text="Пуск- Python",variable=rad, value=1).pack()
ttk.Radiobutton(window,text="Пуск- Python- Python 3.9 IDLE",variable=rad, value=2).pack()
ttk.Radiobutton(window,text="Python- Python 3.9",variable=rad, value=3).pack()
ttk.Radiobutton(window,text="Документы -Python ",variable=rad, value=4).pack()
label1=tk.Label(window,text="2.Python-да жаңа терезе ашу командасы қандай болады?")
label1.pack()
rad1=IntVar()
ttk.Radiobutton(window,text="IDLE ашып, File- New File таңдау керек",variable=rad1, value=1).pack()
ttk.Radiobutton(window,text="IDLE ашып, File- Save таңдау керек",variable=rad1, value=2).pack()
ttk.Radiobutton(window,text="IDLE ашып, File- Exit таңдау керек",variable=rad1, value=3).pack()
ttk.Radiobutton(window,text="IDE ашып, File- New File таңдау керек",variable=rad1, value=4).pack()
label2=tk.Label(window,text="3.Бүтін (int) типке қайсылары жатады?")
label2.pack()
rad2=IntVar()
ttk.Radiobutton(window,text="23",variable=rad2, value=1).pack()
ttk.Radiobutton(window,text="2.5",variable=rad2, value=2).pack()
ttk.Radiobutton(window,text="45",variable=rad2, value=3).pack()
ttk.Radiobutton(window,text="120.88",variable=rad2, value=4).pack()
label3=tk.Label(window,text="4. print қандай функция?")
label3.pack()
rad3=IntVar()
ttk.Radiobutton(window,text="пернетақтадан деректерді енгізу үшін кірістірілген функция",variable=rad3, value=1).pack()
ttk.Radiobutton(window,text="функция мәнін бүтін санға айналдыру функциясы",variable=rad3, value=2).pack()
ttk.Radiobutton(window,text="мәліметті экранға шығару үшін кірістірілген функция",variable=rad3, value=3).pack()
ttk.Radiobutton(window,text="бос программа функциясы",variable=rad3, value=4).pack()
label4=tk.Label(window,text="5. input қандай функция?")
label4.pack()
rad4=IntVar()
ttk.Radiobutton(window,text="пернетақтадан деректерді енгізу үшін кірістірілген функция",variable=rad4, value=1).pack()
ttk.Radiobutton(window,text="функция мәнін бөлшек санға айналдыру функциясы",variable=rad4, value=2).pack()
ttk.Radiobutton(window,text="мәліметті экранға шығару үшін кірістірілген функция",variable=rad4, value=3).pack()
ttk.Radiobutton(window,text="мәліметті экраннан өшіру үшін кірістірілген функция",variable=rad4, value=4).pack()
label5=tk.Label(window,text="6.Жауабы неге тең?  print (3**2)")
label5.pack()
rad5=IntVar()
ttk.Radiobutton(window,text="9",variable=rad5, value=1).pack()
ttk.Radiobutton(window,text="3",variable=rad5, value=2).pack()
ttk.Radiobutton(window,text="2",variable=rad5, value=3).pack()
ttk.Radiobutton(window,text="6",variable=rad5, value=4).pack()
label6=tk.Label(window,text="7.% белгінің сипаттамасы қалай?")
label6.pack()
rad6=IntVar()
ttk.Radiobutton(window,text="бөлу",variable=rad6, value=1).pack()
ttk.Radiobutton(window,text="бөлгендегі қалдық",variable=rad6, value=2).pack()
ttk.Radiobutton(window,text="бүтін санды бөлу",variable=rad6, value=3).pack()
ttk.Radiobutton(window,text="дәрежелеу",variable=rad6, value=4).pack()
label7=tk.Label(window,text="8.Жауабы неге тең?  print (31//6)")
label7.pack()
rad7=IntVar()
ttk.Radiobutton(window,text="1",variable=rad7, value=1).pack()
ttk.Radiobutton(window,text="2",variable=rad7, value=2).pack()
ttk.Radiobutton(window,text="3",variable=rad7, value=3).pack()
ttk.Radiobutton(window,text="5",variable=rad7, value=4).pack()

window.mainloop()