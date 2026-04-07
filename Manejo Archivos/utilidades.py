def mensaje_bienvenida(usuario, passw, nom: None):
    if usuario == "Paul" and passw == "123":
        return f'bienvenido {nom} que bueno tenerte por acá.'
    else:
        return 'Usuario incorrecto'
    
#Calcular el año de nacimiento. - 
def calcular_nacimiento(anio_actual, edad):
    return anio_actual - edad
contador = 0
def contar_vocales(frase):
    global contador
    for i in frase:
        if i in "AEIOUaeiou":
            contador = contador + 1 
    return contador 

print(contar_vocales("Hola mundoo"))