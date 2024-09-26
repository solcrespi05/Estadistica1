# Ejercicio 5
Históricamente el 20% del mercado prefiere el jabón de la marca A.Para incrementar las ventas, la empresa A realiza una intensa campaña de publicidad. Al finalizar la misma se entrevistan 𝑛 = 400 individuos y se les pregunta si prefieren o no la marca A, procurando demostrar que la campaña fue exitosa.
* (a) Expresar $𝐻_0$ y $𝐻_1$ en términos de 𝑝, la probabilidad de que un cliente prefiera el jabón de la marca A al finalizar la campaña. 
* (b) El gerente de la empresa decide concluir que la campaña de publicidad es exitosa si al menos 92 de los 400 clientes entrevistados prefieren la marca A. Especificar cuál es la región de rechazo de la hipótesis nula $𝐻_0$ e indicar, de manera aproximada, cuál es el nivel del criterio propuesto. 
* (c) El dueño de la empresa quiere establecer otro criterio de modo que, con probabilidad 0.05, la campaña se declare exitosa cuando en realidad no lo fue. Construya una región de rechazo para satisfacer al dueño. Si al realizar la encuesta se observa que 92 de los 400 encuestados prefirieron la marca A, calcular de manera aproximada el 𝑝-valor correspondiente a los datos obtenidos. Con estos datos, ¿se rechaza la hipótesis nula a nivel 0.05? 
* (d) Hallar de manera aproximada la probabilidad de cometer un error de tipo II con el criterio propuesto por el dueño si en realidad 𝑝 = 0.24.  

## Resolución 
* a. EL 20% prefiere A, tenemos un total de $n=400$. 
Nuestro $p_0 = 0.2$ , y lo pensamos como:  

    * $H_0 : p \leq p_0$
    * $H_1: p >p_0$

* b. Plantemos el estadístico sabiendo que $\hat{p}=92/400 = 0,23$, entonces nos queda:

$$
T=\frac{0,23-0,2}{\sqrt{\frac{0,2(0,8)}{400}}} = \frac{0,03}{0,02} = 1,5
$$  

Con este valor podemos determinar el nivel significancia. Buscamos el valor de P(Z>1.5).  

$$
Z_{1-\alpha} = 1,5 \\ 1-\alpha = 0,9332 \\ \alpha=0,0668
$$  

* c. Cambiamos el valor de $\alpha =0,05$, por lño que el estadístico nos queda:  

$$
T=\frac{\hat{p}-0,2}{\sqrt{\frac{0,2(0,8)}{400}}} = \frac{\hat{p}-0,20}{0,02}
$$  

Con un $\alpha = 0.05$ nos queda un Z crítico : 

$$
Z_{\alpha} = 1,645
$$  

Resolvemos para $\hat{p}$  

$$
\hat{p}-0,20 = 1,645 * 0,02 \\ \hat{p}=0,20 +0,0329 = 0,2329. 
$$  

La zona de rechazo queda: $R=(p \geq 0,2329)$  

Vemos que el p valor es la probabilidad de obtener un valor de 𝑍 mayor que 1.5 bajo $H_0$:   

$$
P(Z>1,5) = 0,0668
$$  

Y este valor es mayor a 0,05 por lo que no rechazamos $H_0$.  

* d.
Cambiamos el p inicial por $0,24$ , lo que nos deja un Z observado: 

$$
Z= \frac{0,23-0,24}{0,02135} \approx -0.33
$$  

La probabilidad de no rechazar $H_0$: la planteamos $P(Z<-0.33)$

$$
P(Z<-0.33) \approx 0.3707
$$  

Por lo tanto, la probabilidad de cometer un error tipo II es aprox 0.3707