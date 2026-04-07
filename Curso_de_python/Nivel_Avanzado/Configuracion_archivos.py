import pandas as pd

#leer el archivo 

df = pd.read_csv("C:/Users/Paul/OneDrive/Desktop/Progrmar/Curso_de_python/Nivel_Avanzado/Archivo.txt", 
                      sep= ";", 
                      encoding= "utf-8",
                      na_values= ["A/n", "-"],
                      parse_dates= ["Fecha"],
                      dtype= {"Salario":"float64"}, 
                      usecols=["Nombre", "Edad", "Salario", "Fecha"]
                      )
df["Edad"] = df["Edad"].fillna(0).astype("int64")
print(df)

Archivo_limpio = df.to_csv("Archivo_limpio_data.csv", index=False)