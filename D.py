import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos 

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Toplevel()
        self.ventana1.title("PRODUCTOS")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()


    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta producto")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="producto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.producto=tk.StringVar()

        self.entryproducto=ttk.Entry(self.labelframe2, textvariable=self.producto)
        self.entryproducto.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.precio=tk.StringVar()

        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="stock:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.stock=tk.StringVar()

        self.entrystock=ttk.Entry(self.labelframe2, textvariable=self.stock, state="readonly")
        self.entrystock.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        self.entryreserva=ttk.Entry(self.labelframe2)
        self.entryreserva.grid(column=1, row=5, padx=8, pady=8)
        self.boton1=ttk.Button(self.labelframe2, text="reserva", command=self.modifica)
        self.boton1.grid(column=0, row=5, padx=8, pady=8)


    def consultar(self):
        datos=(self.producto.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.precio.set(respuesta[0][0])
            self.stock.set(respuesta[0][1])
        else:
            self.precio.set('')
            self.stock.set('')
            mb.showinfo("Información", "No existe el producto")
    



    def modifica(self):
        datos=(self.stock.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("reserva exitosa")
        else:
            mb.showinfo("indica bien la información")
    

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="STOCK")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="STOCK", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "producto:"+str(fila[0])+"\nprecio:"+fila[1]+"\nstock:"+str(fila[2])+"\n\n")
