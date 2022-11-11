from tkinter import *
import tkinter as tk

from B_categoriatienda2 import lapolar
from B_categoriatienda2 import falabella
from B_categoriatienda2 import hites


#titulo ventana
ventana = tk.Tk()
ventana.title("CENTRO COMERCIAL")
ventana.geometry("358x130")

#tiendas
lblUsuario=Label(text="La polar ",font=("Agency FB", 14)) .place(x=70,y=10)

lblUsuario=Label(text="Falabella ",font=("Agency FB", 14)) .place(x=70,y=40)

lblUsuario=Label(text="Hites ",font=("Agency FB", 14)) .place(x=70,y=70)

#titulo dentro de la ventana
lbl =Label(ventana,text="TIENDAS DISPONIBLES")
lbl.config(bg = "gray")
lbl.pack()

#botones
btn = Button(ventana, text="Mas información", command = lapolar)
btn["fg"]="red"
btn["bg"]="yellow"
btn.pack()

btn = Button(ventana, text="Mas información", command = falabella)
btn["fg"]="red"
btn["bg"]="yellow"
btn.pack()

btn = Button(ventana, text="Mas información", command = hites)
btn["fg"]="red"
btn["bg"]="yellow"
btn.pack()

ventana.mainloop()