inventario ={
    "Manzana" : {"cantidad" : 100, "precio" : 0.50},
    "Bananas" : {"cantidad" : 150, "precio" : 0.30},
    "Naranjas" : {"cantidad" : 80, "precio" : 0.40}
}

def mostrar_inventario(inventario):
    for nombre, detalles in inventario.items(): 
        print(f"Producto:{nombre}, Cantidad:{detalles["cantidad"]}, precio:{detalles["precio"]}")

# def agregar_iventario(inventario, nombre, cantidad, precio): 
#     if nombre in inventario:
#         inventario[nombre]["cantidad"]+= cantidad
#     else:
#         inventario[nombre] ={"cantidad": cantidad, "precio": precio}

def agregar_inventario(inventario, nombre, cantidad, precio):
    if nombre in inventario: 
        inventario[nombre]["cantidad"] += cantidad
    else: 
        inventario[nombre] = {"cantidad": cantidad, "precio":precio}

agregar_inventario(inventario, "pera", 200, 0.10)

def eliminar_producto(inventario, nombre): 
    if nombre in inventario: 
        del inventario[nombre]
    else: 
        print("Producto del inventario no existe")

def actualizar_incentario(inventario, nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre]["cantidad"]= cantidad
        inventario[nombre]["precio"] = precio
    else: 
        print("Producto no existe.")

def consultar_producto(inventario, nombre):
    if nombre in inventario: 
        producto = inventario[nombre]
        print(f"PRODUCTO ENCONTRADO: Producto:{[nombre]}, {producto}")
    else:
        print("Producto no existe.")
    

# eliminar_producto(inventario, "pera")
actualizar_incentario(inventario, "Manzana", 120, 12.0)
nombre_producto = input("Ingrese el nombre del producto: ")
consultar_producto(inventario, nombre_producto)
mostrar_inventario(inventario) 