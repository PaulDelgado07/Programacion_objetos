import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import random
#generar datos aleatorios para calificaciones de 100 estudiantes 
calificiaciones = np.random.normal(loc=75, scale=10, size=100)

calificiaciones = np.clip(calificiaciones, 0,100)

plt.figure(figsize=(10,6))
plt.hist(calificiaciones, bins= 10, color = "skyblue", edgecolor ="black", alpha =0.7)
plt.show()
