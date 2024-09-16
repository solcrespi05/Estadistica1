import numpy as np
import matplotlib.pyplot as plt

#El enunciado pide 100 muestras de una distribucion uniforme en (0,1)
muestras_x = np.random.uniform(0,1,100)

#La funcion f(x) = 2x + 1
muestras_y = 2*muestras_x + 1

#Usamos minimos cuadrados para ajustar los parametros B1 y B0
#Acá tenemos dos formas de hacerlo, una es con la formula de minimos cuadrados y la otra es con np.polyfit
#La formula de minimos cuadrados es:
B1 = np.sum((muestras_x - np.mean(muestras_x))*(muestras_y - np.mean(muestras_y)))/np.sum((muestras_x - np.mean(muestras_x))**2)
B0 = np.mean(muestras_y) - B1*np.mean(muestras_x)
print('B1:', B1)
print('B0:', B0)

#La funcion np.polyfit nos devuelve los coeficientes de la regresion polinomica
beta1,beta0 = np.polyfit(muestras_x, muestras_y, 1)

#calculamos los residuales 
residuales = muestras_y - (beta1*muestras_x + beta0)


# Calcular la media y la varianza de los residuales
media_residuales = np.mean(residuales)
varianza_residuales = np.var(residuales)
print('Media de los residuales:', media_residuales)
print('Varianza de los residuales:', varianza_residuales)

# Graficar el histograma de los residuales
plt.hist(residuales, bins=20, edgecolor='black')
plt.title('Distribución empírica de los residuales')
plt.show()

# Graficar los datos y la recta de regresión
plt.scatter(muestras_x, muestras_y, color='blue')
plt.plot(muestras_x, beta1*muestras_x + beta0, color='red')
plt.title('Recta de regresión')
plt.show()