"""
OPERADORES LOGICOS
"""
#and: devielve True si ambas expresiones son verdaderas 
#or: devielve True si al menos una de las expresiones es verdadera 
#not: Niega la expresión Booleana; devuelve False si la expresión es verdadera o viceversa

nombre_persona = "Juan"
nombre_empleado = "Juan"
esta_logueado=False

respuesta2 = True != esta_logueado

respuesta = nombre_persona == nombre_empleado
#print(respuesta2)

edad_persona = 16
tiene_licencia = True 
puede_conducir = edad_persona >=18 or tiene_licencia
#print(puede_conducir)

a = 10 
b = 20
c = 10 

print(a == b) #false 
print(a != b) #true 
print(a > b) #false 
print(a < b) # true 
print(a >= c) # true 
print(a <= c) # true 

if a <= b and a == c: 
    print("a es menor igual a b y a es igual a c ")
else: 
    print("la condicion no cumple")