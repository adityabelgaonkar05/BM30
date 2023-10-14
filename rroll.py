python


import webbrowser
from tkinter import*
root=Tk()
ty=10
bet1="=dQw"
bet2="WgX"
first="http"
between_middle="out"
between_last="atch?v"
middle="s://www.y"+between_middle+"ube.c"
last="om/w"+between_last+bet1+"4w9"+bet2+"cQ"


def rr():
    th=0
    while th<=ty:
        webbrowser.open_new(first+middle+last)


rbutton=Button(root,text="Press Me, u/Boom2005",fg="red",command=rr)
rbutton.pack()
root.mainloop()