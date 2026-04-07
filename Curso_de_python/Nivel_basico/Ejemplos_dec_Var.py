#Ejemplos varios de declaracion de variables
#Asigancion simple: 

nom_per = "Armando"
ape_per= 'Ruiz'
edad_per= 49
sue_per = 1200.98
act_per = True 

#asignaciones multiples 

cant_prod , msj_bien , estado =  5, "Hola", True 
#print(msj_bien)

#asignar el mismo valor a varias variables
x = y = z = 10 
#print(x,y,z)

#tipos de datos especiales (estructura de datos)
"""
LIST 
DICCIONARIOS 
TUPLAS 
CONJUNTOS
"""
cursos = ["Python", "DJanco", "Flask", 20,230.70, True, ["Fastapi", "Pandas"]] #listas 

empleados = {
    "codigo":"200", 
    "Nombre":"Juan", 
    "Apellido":"Ruiz", 
} #dic 

valores=(100,200,300) #tuplas, no se puede agregar ni eliminar porque ya están estructuradas 

datos = {12, 45, 36, 56, 34}
print(datos)

print(empleados["Nombre"])

import keyword 

print(keyword.kwlist)

empleado_nom = "Armando"

print(keyword.iskeyword(empleado_nom))