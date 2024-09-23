# Ejercicio 8
La nota de una prueba de aptitud sigue una distribución normal. Una muestra aleatoria de nueve alumnos de la ciudad arroja los siguientes resultados: 5, 8.1, 7.9, 3.3, 4.5, 6.2, 6.9, 7.5, 9.1.
* (a) Hallar un intervalo de confianza para la nota media de los alumnos de la ciudad.
* (b) La nota media de todos los alumnos de la ciudad en ese mismo examen el año anterior es 7.50. ¿Le parece que hay motivos para afirmar que la nota media de los alumnos ha cambiado con respecto al año anterior?

## Resolución
* a. Plantemos las variables que tenemos.  
    * n = 9
    * $\mu = 6,5$
    * $s = \sqrt{\frac{1}{n}\sum(x_i-\bar{x})^{2}} = 1,873$  

Tenemos que usar t-student  

$$
IC = \left(\bar{x} - t_{1-\alpha/2}.\frac{s}{\sqrt{n}} \right) = 1- \alpha
$$  

Si proponemos un $\alpha =0,05 \ \Rightarrow \frac{\alpha}{2} = 0,025$  

$$
IC= \left(6,5 \pm t_{0.25,8} \frac{1,873}{3} \right) = \left(6,5 \pm 2,308 \frac{1,873}{3} \right)
$$  

$$
IC = (5.060 ; 7,937 )
$$  
