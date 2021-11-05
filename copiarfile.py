

from tkinter import *
from tkinter import ttk

def enable(childList):
    for child in childList:
        child.configure(state='enable')

root = Tk()

#Creates top frame
frame1 = ttk.LabelFrame(root, padding=(10,10,10,10))
frame1.grid(column=0, row=0, padx=10, pady=10)

button2 = ttk.Button(frame1, text="This enables bottom frame", 
                     command=lambda: enable(frame2.winfo_children()))
button2.pack()

#Creates bottom frame
frame2 = ttk.LabelFrame(root, padding=(10,10,10,10))
frame2.grid(column=0, row=1, padx=10, pady=10)

entry = ttk.Entry(frame2)
entry.pack()

button2 = ttk.Button(frame2, text="button")
button2.pack()

for child in frame2.winfo_children():
    child.configure(state='disable')

root.mainloop()