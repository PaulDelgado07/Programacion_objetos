import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import random 

np.random.seed(42)
#fechas para el mes de enero
fechas = pd.date_range(start= "2024-01-01", end = "2024-01-31")

#generar datos de ventas de manera aleatoria
ventas = np.random.randint(50, 200, size=len(fechas))
print(ventas)

productos = np.random.choice(["PRODUCTO A", "PRODUCTO B", "PRODUCTO C"], size=len(fechas))

df_ventas = pd.DataFrame({
    "Fechas" : fechas,
    "Productos" : productos,
    "Ventas" : ventas
})

#agrupar por fecha y vamos a sumar las ventas

# ventas_diarias = df_ventas.groupby('Fechas')['Ventas'].sum().reset_index()
# print(ventas_diarias)

#crear un grafico de lineas para las ventas diarias para seguir el seguimiento 
# plt.figure(figsize=(10,5))
# plt.plot(ventas_diarias["Fechas"], ventas_diarias["Ventas"], marker = "o", color = "red")
# plt.title("Ventas de la fecha de enero", color = "green")
# plt.xticks(rotation = 45)
# plt.grid(True)
# plt.tight_layout()
# plt.xlabel("Fechas")
# plt.ylabel("Ventas")
# plt.show()

#productos y sumar las ventas. - 
sumar_ventas = df_ventas.groupby("Productos")["Ventas"].sum().reset_index()
print(sumar_ventas)

#Generador de imagenes
plt.figure(figsize=(12,5))
plt.bar(sumar_ventas["Productos"], sumar_ventas["Ventas"], color = "Red")
plt.xlabel("Productos")
plt.ylabel("Total de Ventas")
plt.title("Ventas totales por productos", color= "Red")
plt.xticks(rotation = 50)
plt.grid(axis="y")
plt.show()

