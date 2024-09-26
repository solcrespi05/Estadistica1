# Ejercicio 3
En 1000 tiradas de moneda aparecen 560 caras y 440 cecas. ¿Es razonable suponer que la moneda es justa, es decir que la probabilidad de cara y de ceca son iguales?

## Resolución
Vemos que en este problema se pone en juego la distribución Bernoulli, la cual tiene un parámetro p .Que en este caso es el que vamos a usar para plantear la hipótesis. 

Planteamos la hipótesis y las variables que tenemos:  
* $H_0: p=p_0 = 0.5$
* $H_1: p\neq 0.5$
* $n=1000$

El estadistico que vamos a usar es:  

$$
T=\frac{\bar{x} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$  

$$
T=\frac{\bar{x} - 0,5}{\sqrt{\frac{0,5(0,5)}{1000}}} =\frac{\bar{x}-0,5}{0,016}
$$  

nuestro $\bar{x}$ va a ser la propoción de caras con respecto del total $\rightarrow \bar{x}= \frac{560}{1000} = 0,56$  

$$
=\frac{0,56-0,5}{1000} = 3,79
$$  

Si planteamos un nivel de significancia del 0.05 y es un test bilateral ( porque es $\neq$ la hipotesis alternativa), el valor crítico de Z seria aproximadamente : $Z_{\alpha/2} = Z_{0.975} = 1.96 $  

Planteamos la zona de rechazo como : 

$$
RR=(|Z|>1,96)
$$

En nuestro caso $Z=3,79$ , por lo que como es mayor rechazamos $H_0$.  

