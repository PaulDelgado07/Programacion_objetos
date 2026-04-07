"""
Metodos de instancia
"""

class circulo: 
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * (self.radio ** 2)
    
    def cambiar_radio(self, nuevo_radio):
        self.radio = nuevo_radio
        

mi_circulo = circulo(5)
mi_circulo.cambiar_radio(10)

print(f"area del circulo {mi_circulo.area():.2f}")
print(f"nuevo area del circulo {mi_circulo.area():.2f}")