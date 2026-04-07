import json 
import pandas as pd 

# cars = [
#     {"nombre": "honda", "price": 10000, "model": 2020, "power": 13000},
#     {"nombre": "toyota", "price": 12000, "model": 2021, "power": 15000},
#     {"nombre": "Audi", "price": 150000, "model": 2022, "power": 17000},
#     {"nombre": "Ford", "price": 18000, "model": 2020, "power": 20000},
# ]

# print(cars)

# with open("e:/Users/Paul/OneDrive/Desktop/informacioncars.json", "r") as f:
#     json.dump(cars , f)

df_iris = pd.read_csv("C:/Users/Paul/OneDrive/Desktop/Progrmar/Curso_de_python/Nivel_Avanzado/iris.json")
print(df_iris.head())