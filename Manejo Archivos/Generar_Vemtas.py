#Generar ventas de los productos 
def generar_registro_ventas(producto, precio, cantidad): 
    with open("ventas.txt", "a") as archivo:
        total = precio * cantidad
        archivo.write(f"Producto: {producto}, Precio: {precio}, Cantidad: {cantidad}, Total: {total}\n")
    print(f"Producto: {producto}, Precio: {precio}, Cantidad: {cantidad}, Total: {total}\n")

generar_registro_ventas("Producto 1", 10, 5)
generar_registro_ventas("Producto 2", 20, 3)
generar_registro_ventas("Producto 3", 15, 2)
generar_registro_ventas("Producto 4", 5, 10)
generar_registro_ventas("Producto 5", 30, 1)

