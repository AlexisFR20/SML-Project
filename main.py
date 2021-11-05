import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


label = tk.Label(root, text="INSTALACION LMS")  # Create a text label
label.pack(padx=20, pady=20)


checkframe = tk.Frame(root)
checkframe.pack(side="top")
checkframe.config(bg = 'blue')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(checkframe, text='Permisos de administrador',
                    variable=var1, onvalue=0, offvalue=0)
c1.pack(side="left")
c2 = tk.Checkbutton(checkframe, text='User Account Control: Run all administrators in Admin Approval Mode: Disable',
                    variable=var2, onvalue=0, offvalue=0)
c2.pack(side="left")


ancho_ventana = root.winfo_screenwidth() - (root.winfo_screenwidth()*0.25)
alto_ventana = root.winfo_screenheight() - (root.winfo_screenheight()*0.25)

ancho_ventana = round(ancho_ventana)
alto_ventana = round(alto_ventana)

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)


root.mainloop()
