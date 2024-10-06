import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

age_data = df['Age'].dropna().tolist()
weight_data = df['Weight (kg)'].dropna().tolist()
bmi_data = df['BMI'].dropna().tolist()

media_edad = np.mean(age_data)
mediana_edad = np.median(age_data)
moda_edad = stats.mode(age_data)[0][0]

media_peso = np.mean(weight_data)
mediana_peso = np.median(weight_data)
moda_peso = stats.mode(weight_data)[0][0]

media_bmi = np.mean(bmi_data)
mediana_bmi = np.median(bmi_data)
moda_bmi = stats.mode(bmi_data)[0][0]

print(f"Edad - Media: {media_edad}, Mediana: {mediana_edad}, Moda: {moda_edad}")
print(f"Peso - Media: {media_peso}, Mediana: {mediana_peso}, Moda: {moda_peso}")
print(f"BMI - Media: {media_bmi}, Mediana: {mediana_bmi}, Moda: {moda_bmi}")

# 1Edad:
# La media es de 38.68 años, lo que indica que la mayoría de los individuos tienen una edad cercana
# a los 40 años, la mediana es de 40, lo que sugiere que la distribución de la edad es simétrica,
# la moda es 43, lo que indica que es la edad más frecuente en el conjunto de datos.

# 2Peso (Weight)
# La media del peso es 73.85 kg, lo que indica que el peso promedio es de aproximadamente 74 kg
# , la mediana es de 70 kg, lo que sugiere que hay más individuos con pesos menores que el
# promedio, y la moda es 57.7 kg, lo que muestra que un gran número de personas tiene un peso alrededor de este valor.

# 3BMI
# La media del BMI es de 24.91, lo que indica que la mayoría de los individuos tienen un índice de masa corporal cercano al rango
# "normal", la mediana es de 24.16, lo que sugiere que la mayoría de los valores se concentra
# n en el rango saludable.La moda es 23.53, lo que indica que es el valor de BMI más común.

data = [age_data, weight_data, bmi_data]
plt.boxplot(data, labels=['Age', 'Weight (kg)', 'BMI'])
plt.title('Diagrama de Cajas y Bigotes para Edad, Peso y BMI')
plt.ylabel('Valores')
plt.grid(True)
plt.show()

# gráfico
# El gráfico de cajas y bigotes muestra la dispersión de los datos y los valores
# atípicos, en la columna "Peso", se observan valores atípicos por encima de 120 kg,
# el "BMI" también tiene algunos valores atípicos que exceden el rango normal (>35), indicando obesidad en
# algunos casos. Para la "Edad", no hay valores atípicos significativos, con una distribución más uniforme entre 20 y 60 años.
