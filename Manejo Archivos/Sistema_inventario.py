"""
Docstring for Manejo Archivos.Sistema_inventario
- Dos almacenes
 -Realizar operaciones en esos dos alamecenes.
 -Encontrar productos comunes
 -Encontrar Productos exclusivos de cada almacen 
 -Lista completa de todos los productos disponibles en ambos almacenes
"""
alamacen_1 = {"laptop", "mouse", "teclado", "monitor", "impresora"}
alamacen_2 = {"laptop", "monitor", "tablet", "smartphone", "impresora"}

#productos mas comunes. -
print(f"Los productos mas comunes son:{alamacen_1 & alamacen_2}")

#encontrar productos exclusivos de cada almacen. - 
print(f"Productos exclusivos del alamacen 1: {alamacen_1 - alamacen_2}")
print(f"Productos exclusivos del alamacen 2: {alamacen_2 - alamacen_1}")

#lista completa de todos los almacenes
print(f"Productos completos de los dos almacenes: {alamacen_1.union(alamacen_2)}")