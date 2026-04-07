import pandas as pd

# df = pd.DataFrame({
#     "Nombre" : ["Ana", "Carlos", "Beatriz", "David"],
#     "Edad" : [23, 35, 29, 40], 
#     "Salario" : [5000.5, 70000.8, 65000.3, 80000.0]
# })

# Save_excel = df.to_excel("Archivo_Excel.xlsx", sheet_name= "Empleados", index = False)

Leer_empleados = pd.read_excel("C:/Users/Paul/OneDrive/Desktop/Progrmar/Curso_de_python/Nivel_Avanzado/Archivo_Excel.xlsx")

df = pd.DataFrame(Leer_empleados)
print(df)