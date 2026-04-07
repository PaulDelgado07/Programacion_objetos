# dado una fecha de nacimiento, calcular la edad actual. 

from datetime import date 

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year

    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -=1 

    return edad

fecha_nacimiento = date(2005, 8, 19)

print(calcular_edad(fecha_nacimiento))
