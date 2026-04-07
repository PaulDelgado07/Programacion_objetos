class vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca 
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_información(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}"

class coche(vehiculo): 
    def __init__(self, marca, modelo, anio, numeros_puertas):
        super().__init__(marca, modelo, anio)
        self.numeros_puertas = numeros_puertas
    
    def mostrar_información(self):
        base_info = super().mostrar_información()
        return f"{base_info}, puertas: {self.numeros_puertas}"
    
class motocicleta(vehiculo):
    def __init__(self, marca, modelo, anio, motor):
        super().__init__(marca, modelo, anio)
        self.motor = motor

    def mostrar_información(self):
        base_info_moto = super().mostrar_información()
        return f"{base_info_moto}, motor: {self.motor}"