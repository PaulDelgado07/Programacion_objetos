"""🧠 Ejercicio: Clase Persona con verificación de edad
🎯 Objetivo:
Crear una clase Persona que:
Guarde el nombre y la edad.
Tenga un método para saludar.
Tenga un método que diga si la persona es:
niño (0-12)
adolescente (13-17)
adulto (18--59)
adulto mayor (60+)"""

class persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def informacion(self):
        print(f"Yo soy {self.nombre} y tengo {self.edad} años y soy un {self.edades()}")

    def saludar(self):
        print(f"{self.nombre}dice Hola.")

    def edades(self):
        if self.edad <= 12: 
            return "niño"
        elif self.edad <= 17:
            return "adolescente"
        elif self.edad <= 59:
            return "adulto"
        else: 
            return "adulto mayor"

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad de la persona: ")) 
p1 = persona(nombre,edad)
print("_____________")
p1.saludar()
print("_____________")
p1.informacion()