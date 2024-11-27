import tkinter as tk

inventario = {}

def validar_nombre_producto(nombre):
    if nombre == "":
        raise Exception("El nombre del producto no puede estar vacío.")
    
def validar_precio_producto(precio):
    if precio <= 0:
        raise Exception("El precio del producto debe ser mayor que cero.")
    
def validar_cantidad_producto(cantidad):
    if cantidad < 0:
        raise Exception("La cantidad del producto debe ser mayor o igual a 0.")

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        validar_nombre_producto(nombre)
        precio = float(entry_precio.get())
        validar_precio_producto(precio)
        cantidad = int(entry_cantidad.get())
        validar_cantidad_producto(cantidad)

        if nombre in inventario:
            inventario[nombre]["Cantidad"] += cantidad
            inventario[nombre]["Total"] += (precio * cantidad)
        else:
            inventario[nombre] = {
                "Precio": precio,
                "Cantidad": cantidad,
                "Total": (precio * cantidad)
            }

        mensaje = (
            f"Producto: {nombre}\n"
            f"Precio Unitario: ${precio:.2f}\n"
            f"Cantidad en Inventario: {inventario[nombre]['Cantidad']}\n"
            f"Valor Total en Inventario: ${inventario[nombre]['Total']:.2f}"
        )
        label_mensaje.config(text=mensaje)

    except Exception as e:
        label_mensaje.config(text=str(e))

ventana = tk.Tk()
ventana.title("Tiendita")
ventana.geometry("300x250")

tk.Label(ventana, text="Producto:").place(x=20, y=20)
tk.Label(ventana, text="Precio:").place(x=20, y=60)
tk.Label(ventana, text="Cantidad:").place(x=20, y=100)

entry_nombre = tk.Entry(ventana)
entry_nombre.place(x=100, y=20)
entry_precio = tk.Entry(ventana)
entry_precio.place(x=100, y=60)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.place(x=100, y=100)

btn_agregar = tk.Button(ventana, text="Agregar a inventario", command=agregar_producto)
btn_agregar.place(x=80, y=150)

label_mensaje = tk.Label(ventana, text="")
label_mensaje.place(x=20, y=180)

ventana.mainloop()