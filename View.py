import tkinter as tk
import ctypes
import os
from sys import exit
import json

import shutil


# GENERACION DE VENTANA
root = tk.Tk()

title = tk.Label(root, text="INSTALACIÓN LMS")
title.pack()
title.configure(font=(26))


def is_disabled():
    fuente = "//MHQ-80-1245/JessyShare/hosts"
    # Cuando se lanze la aplicacion:
    #   - Modificar ruta a C:\Windows\System32\drivers\etc\hosts
    destino = "C:/Users/afrancoreyes/Desktop/hosts"
    global DISABLED
    try:
        shutil.copyfile(fuente, destino)
        c2.select()
    except:
        c2.deselect()


def is_admin():
    global ADMIN
    is_admin = False
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if(is_admin):
        c1.select()
    else:
        c1.deselect()


def openConfig(permission):
    with open('data.json') as file:
        data = json.load(file)
    # print("Permisson: {}".format(permission))
    if(permission == "admin"):
        if(int(data['config'][0]["admin"]) == 0):
            c1.select()
        else:
            c1.deselect()
    if(permission == "disabled"):
        if(int(data['config'][0]["disabled"]) == 0):
            c2.select()
        else:
            c2.deselect()

# # FRAME de validaciones
checkframe = tk.Frame(root)
checkframe.pack(side='top')
subtitle = tk.Label(checkframe, text="Requerimientos previos")
subtitle.configure(font=(11))
subtitle.grid(column=1, row=1)


vc1 = tk.IntVar(checkframe)
vc2 = tk.IntVar(checkframe)

c1 = tk.Checkbutton(checkframe, text='El usuario es administrador',
                    variable=vc1, state="disabled")
c1.grid(column=1, row=2)

c2 = tk.Checkbutton(checkframe, text='User Account Control: Run all administrators \nin Admin Approval Mode: [Disable]',
                    variable=vc2, state="disabled")
c2.grid(column=2, row=2)

def check():
    is_disabled()
    is_admin()
    # openConfig("admin")
    # openConfig("disabled")

boton = tk.Button(
    checkframe, text="Verificar \nconfiguraciones", command=check)
boton.grid(column=3, row=2)


# FRAME de CONFIGURACION
conframe = tk.Frame(root)
conframe.pack()
subtitle = tk.Label(conframe, text="CONFIGURACION")
subtitle.configure(font=(11))
subtitle.grid(column=2, row=1)

vc1 = tk.IntVar(conframe)
vc2 = tk.IntVar(conframe)

c1 = tk.Checkbutton(conframe, text='El usuario es administrador',
                    variable=vc1, state="disabled")
c1.grid(column=1, row=2)

c2 = tk.Checkbutton(conframe, text='User Account Control: Run all administrators \nin Admin Approval Mode: [Disable]',
                    variable=vc2, state="disabled")
c2.grid(column=2, row=2)


# Configuracion de ventana
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
