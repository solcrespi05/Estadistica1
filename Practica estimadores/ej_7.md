# Ejercicio 7
Se supone que la longitud en milímetros de cierto tipo de eje tiene una distribución normal con desvío estándar 𝜎 = 0.05. Se toma una muestra de 20 ejes y se observa que la longitud media de los ejes es de 52.3.
- (a) Hallar un intervalo de confianza para la verdadera longitud media de nivel 0.99.
- (b) ¿Qué tamaño debe tener la muestra para que la longitud de un intervalo de nivel 0.99 sea a lo sumo 0.03?  

## Resolución

- a. Definimos las variables que nos da el enunciado:  

    * n= 20
    * $\mu = 52.3$
    * $\sigma^{2} = 0.05$
    * $\sigma = 0.2236$  
    * $\alpha = 0.01$

Nuestro estadístico es :  

$$
Z = \frac{\bar{x}-\mu}{\sigma}. \sqrt{n}
$$  

Entonces el intervalo de confianza nos queda:  

$$
IC=\bar{x} \pm Z_{(1-\alpha/2)}. \frac{\sigma}{\sqrt{n}}
$$  

$$
IC= 52,3 \ \pm Z_{0,995}.\frac{0,2236}{\sqrt{20}} = 52,3 \ \pm 2,58.\frac{0,2236}{4,47}
$$  

$$
IC=(52.1709;52.429)
$$  

* b. Necesitamos saber que cantidad de muestras necesitamos para que la longitud del intervalo de nivel 0.99 sea a lo sumo 0.03.  
ES decir, necesitamos que el total de nuestro estadístico sea de 0.03. Por lo que planteamos:  

$$
2E = 0,03 \ \Rightarrow E = 0,015
$$  

$$
 0,015  =2,58 . \frac{0,05}{\sqrt{n}} \ \Rightarrow \sqrt{n} = \frac{2,58 . 0,05}{0,015}
$$  

$$
n = 8,6^{2} \ \Rightarrow n=73,96 \sim 74
$$  

Entonces necesitamos una 74 muestras en total.  

