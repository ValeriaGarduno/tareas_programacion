import tkinter as tk
from tkinter import messagebox

class ExcepcionProducto(Exception):
    
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_nombre(nombre):
    if nombre == "":
        raise ExcepcionProducto("El nombre del producto no puede estar vacío")
    
def validar_precio(precio):
    if precio <= 0:
        raise ExcepcionProducto("El precio del producto debe ser mayor que cero")
    
def validar_cantidad(cantidad):
    if cantidad < 0:
        raise ExcepcionProducto("La cantidad del producto debe ser mayor que cero")

inventario = {}

def agregar_producto(): 
        try:
            nombre = str(entry_nombre.get())
            validar_nombre(nombre=nombre)
            precio = float(entry_precio.get())
            validar_precio(precio=precio)
            cantidad = int(entry_cantidad.get())
            validar_cantidad(cantidad=cantidad)
             
            if nombre in inventario:
                inventario[nombre] += cantidad  
            else:
                inventario[nombre] = cantidad
            
            valor = inventario[nombre] * precio

            info= f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Valor Total: {valor}"

            label_detalles.config(text=info)
            
        except ExcepcionProducto as e:
            label_detalles.config(text=f"Error: {e}")            


ventana = tk.Tk()
ventana.title("Tiendita")
ventana.geometry("300x300")

label_nombre = tk.Label(ventana, text="Nombre :")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)
    
label_precio = tk.Label(ventana, text="Precio:")
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack(pady=5)

label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=5)
    
boton_mostrar_detalles = tk.Button(ventana, text="Mostrar Detalles", command= agregar_producto)
boton_mostrar_detalles.pack(pady=10)
    
label_detalles = tk.Label(ventana, text="", justify="left", anchor="w")
label_detalles.pack(pady=10)

ventana.mainloop()



