from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

from C_tiposdeproductos import categorialapolar
from C_tiposdeproductos import categoriafalabella
from C_tiposdeproductos import categoriahites

def lapolar():
    top= tk.Toplevel()
    top.title('La polar')
    top.geometry("560x200")

    btn = tk.Button(top, text='Tienda online "categorias"', command = categorialapolar)
    btn.pack( side = BOTTOM)

    label1= Label(top, text='Multienda dedicada a la venta de todos los productos necesarios para su hogar y su familia.',font=("Agency FB", 14)) .place(x=0,y=0)
    label1= Label(top, text='Ubicación: Segundo piso, sector 3',font=("Agency FB", 14)) .place(x=70,y=40)
    label1= Label(top, text='Horario: Lunes ha Domingo 10:00 - 18:50 HRS.',font=("Agency FB", 14)) .place(x=70,y=70)
    
    imagen=PhotoImage(file="imagen\lapolar.png")
    top=Label(top,image=imagen).place(relx=.4,rely=.5)
    top.mainloop()


def falabella():
    top= tk.Toplevel()
    top.title('Falabella')
    top.geometry("560x200")

    btn = tk.Button(top, text='Tienda online "categorias"', command = categoriafalabella)
    btn.pack( side = BOTTOM)

    label1= Label(top, text='Multienda dedicada a la venta de todos los productos necesarios para su hogar y su familia.',font=("Agency FB", 14)) .place(x=0,y=0)
    label1= Label(top, text='Ubicación: Segundo piso, sector 3',font=("Agency FB", 14)) .place(x=70,y=40)
    label1= Label(top, text='Horario: Lunes ha Domingo 10:00 - 18:50 HRS.',font=("Agency FB", 14)) .place(x=70,y=70)
    
    imagen=PhotoImage(file="imagen\lapolar.png")
    top=Label(top,image=imagen).place(relx=.4,rely=.5)


def hites():
    top= tk.Toplevel()
    top.title('Hites')
    top.geometry("560x200")

    btn = tk.Button(top, text='Tienda online "categorias"', command = categoriahites)
    btn.pack( side = BOTTOM)

    label1= Label(top, text='Multienda dedicada a la venta de todos los productos necesarios para su hogar y su familia.',font=("Agency FB", 14)) .place(x=0,y=0)
    label1= Label(top, text='Ubicación: Segundo piso, sector 3',font=("Agency FB", 14)) .place(x=70,y=40)
    label1= Label(top, text='Horario: Lunes ha Domingo 10:00 - 18:50 HRS.',font=("Agency FB", 14)) .place(x=70,y=70)
    
    imagen=PhotoImage(file="imagen\lapolar.png")
    top=Label(top,image=imagen).place(relx=.4,rely=.5)

