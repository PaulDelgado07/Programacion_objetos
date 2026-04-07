class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}"
    
#creacion de un objeto de la clase persona

persona1 = persona("Paul", 20)
persona2 = persona("Maria", 30)
# print(f"Mi nombre es {persona1.nombre} y mi edad es {persona1.edad}")
# print(persona1.__dict__)
print(persona2.saludar())