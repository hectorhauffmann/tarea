from tkinter import *
import tkinter as tk
from D import FormularioArticulos

def categorialapolar():
    top= tk.Toplevel()
    top.title('La polar')
    top.geometry("200x200")

    btn = tk.Button(top, text='electrodomestico', command = FormularioArticulos)
    btn.pack( )

    btn = tk.Button(top, text='telefono')
    btn.pack( )

    btn = tk.Button(top, text='gaming')
    btn.pack( )

def categoriafalabella():
    top= tk.Toplevel()
    top.title('La polar')
    top.geometry("560x200")

    btn = tk.Button(top, text='electrodomestico')
    btn.pack( )

    btn = tk.Button(top, text='telefono')
    btn.pack( )

    btn = tk.Button(top, text='gaming')
    btn.pack( )

def categoriahites():
    top= tk.Toplevel()
    top.title('La polar')
    top.geometry("560x200")

    btn = tk.Button(top, text='electrodomestico')
    btn.pack( )

    btn = tk.Button(top, text='telefono')
    btn.pack( )

    btn = tk.Button(top, text='gaming')
    btn.pack( )