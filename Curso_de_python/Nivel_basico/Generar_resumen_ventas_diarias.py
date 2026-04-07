"""
Descripcion:
dado un registo de ventas diarias en una lista de diccionarios, generar 
un resumen con total de ventas y la cantidad de articulos vendidos.
"""
# def resumen_ventas(ventas): 
#     total_ventas = 0 
#     total_articulos = 0 
#     #paso 2 
#     for i in ventas: 
#         total_ventas += i['precio'] * i['cantidad']
#         total_articulos += i['cantidad']
    
#     return total_ventas, total_articulos

# ventas =[
#     {'precio' : 10, 'cantidad': 2},
#     {'precio' : 5, 'cantidad': 4},
#     {'precio' : 20, 'cantidad': 1},
# ]

# print(resumen_ventas(ventas))
    

ventas =[
    {'precio' : 10, 'cantidad': 2},
    {'precio' : 5, 'cantidad': 4},
    {'precio' : 20, 'cantidad': 1},
]

def resumen_ventas(ventas): 
    total_ventas = 0 
    total_cantidad = 0 
    
    for i in ventas: 
        total_ventas += i['precio'] * i['cantidad']
        total_cantidad += i['cantidad']

    return total_cantidad, total_ventas 

print(resumen_ventas(ventas))