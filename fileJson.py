# import json
# data = {}
# data['config'] = []
# data['config'].append({
#     'admin': '1',
#     'disabled': '1'})
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

import tkinter  as tk 
root = tk.Tk()
root.geometry("300x150")

def my_upd():
    if(c4_v.get()==1):
        c4.deselect()   
    else:
        c4.select()   
    
c1=tk.Checkbutton(root,text='Main',command=my_upd,font=18)
c1.grid(row=1,column=1)

c4_v=tk.IntVar()
c4=tk.Checkbutton(root,text='Copy',font=18,variable=c4_v)
c4.grid(row=1,column=2)
root.mainloop()