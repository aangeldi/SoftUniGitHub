
from tkinter import *
from tkinter.ttk import *

ws = Tk()
ws.title("Python Guides")

entry1 = Entry(ws)
entry1.pack(expand = 1, fill = BOTH)

entry2 = Button(ws, text ="Button")

entry2.focus_set()
entry2.pack(pady = 5)

entry3 = Radiobutton(ws, text ="Hello")
entry3.pack(pady = 5)

ws.mainloop()