# Ejercicio 2 
Según una encuesta, la cantidad de minutos que le lleva a un alumno de la facultad llegar al campus en tren es una variable aleatoria normal de media 𝜇 = 45 y varianza 𝜎2 = 144. Se quiere saber si quienes vienen en colectivo tardan más. 
- (a) Plantear el test de hipótesis adecuado. En base a una muestra aleatoria de 100 datos, dar las regiones de rechazo de nivel 𝛼1 = 0.01 y de nivel 𝛼2 = 0.05 
- (b) Se sabe que, para una muestra de 100 datos, se rechazó la hipótesis nula a nivel 0.05, pero no a nivel 0.01. Indicar qué valores puede tomar el promedio muestra. 
- (c) En un test de nivel 0.05 basado en una muestra de 100 datos,¿cuál es la probabilidad de no rechazar 𝐻0 si en realidad 𝜇 = 48 minutos? 
- (d) Calcular el tamaño de la muestra que se debe considerar si se quiere rechazar la hipótesis nula a nivel 0.01 en el caso en que el promedio muestral sea 47 minutos.

## Resolución 
* a. Planteamos las variables que tenemos:  
    - $\bar{X} \sim N(45,144)$
    - $\mu = 45$
    - $\sigma ^{2} = 144$
    - $H_0 : \mu = 45$
    - $H_1: \mu> 45$
    - $n=100$

Vemos las regiones de rechazo para ambos $\alpha$:  
**$\alpha_1 = 0.01$**

$$
T \Rightarrow Z = \frac{\bar{x}-45}{12/10} = \frac{\bar{x}-45}{1,2}
$$  

$$
Z_{1-0,01} = Z_{0,99} = 2,33
$$  

$$
2,33 = \frac{c-45}{1,2} \Rightarrow 2,33 \ . \ 1,2 =c-45 \\ c = 2,796+45 = 47,796
$$  

La región de rechazo nos queda: $R = (47,796 ; +\infty)$  

**$\alpha_2 = 0.05$**  

$$
Z_{0.95} = 1.64
$$  

$$
1,64 = \frac{c- 45}{1,2} \Rightarrow 1,968+45=c 
$$  

$$
c= 46,968
$$  

La region de recho para el $\alpha_2$ nos queda : $R= (46,968; + \infty)$  


* b. Puede tomar el siguiente rango de valores para que se rechace la hipótesis nula : $(46,968 \ ; \ 47,796)$  

* c. Queremos calcular la probabilidad de no rechazar $𝐻_0$ si en realidad $𝜇=48$ minutos, es decir, si $𝜇_{verdadero}=48$  


Esta probabilidad es conocida como el error tipo II o β.  
La probabilidad de rechazar $H_0$ es la potencia del test, entonces $β=1−Potencia$.  
Para calcular la potencia cuando $\mu =48$, usamos la fórmula del estadictico y nos queda:  

$$
Z= \frac{\bar{X}-48}{1,2}
$$  

Queremos la probabilidad de no rechazar $H_0$, es decir, que Z esté por debajo del valor crítico para $\alpha = 0.05$, que es $Z=1.645$.  

$$
P\left(Z<\frac{1,64 . 1,2+45 -48}{1,2} \right )  = P(Z<-2,355) \approx 0,0093
$$  

Por lo tanto la probabilidad de no rechazar $H_0$ es aproximadament 0,0093.  

* d. Calculamos con el $\alpha = 0.01$  

$$
2,33 = \frac{47-45}{12/ \sqrt{n}} \Rightarrow 2,33 = \frac{2}{12/\sqrt{n}}
$$  

$$
\sqrt{n} = \frac{2,33 . 12}{2} \approx 13,98 
$$  

$$
n= 195,4
$$  


Entonces necesitariamos 196 muestras para rechazar la muestra a nivel $\alpha = 0.01$ Tomando como media 47 minutos.  

