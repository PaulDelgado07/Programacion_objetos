#clases de funciones 


def sumar(a,b):
    return a + b

print(sumar(2,2))

def mensaje_bienvenida(nombre):
    print(f"Hola,{nombre} contento de que estés aqui.")
mensaje_bienvenida("Paul")

suma = lambda x, y: x + y
print(suma(2,4))

#funciones anidadas
def resultados_minimos(x,y):
    def suma(x,y):
        return x+y
    def resta(x,y): 
        return x-y
    
    return suma(x,y), resta(x,y)

re_sum, re_resta= resultados_minimos(10,9)
print(f"resultado de la suma es: {re_sum}, y el resultado de la resta es: {re_resta}")