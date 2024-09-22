# Ejercicio 2
Generar 100 observaciones de una distribución N (0, 1) y calcular un intervalo de confianza del
95% para la función de distribución acumulada 𝐹 .
Repetir esto 1000 veces y calcular la cuántas veces el intervalo de confianza contiene la verdadera función de distribución.

## Resolución
Primero definimos los valores que tenemos.   
* n= 100  
* Distribución Normal
* IC = 95% --> $\alpha = 0.05$

Lo que buscamos es  
$$P(-Z_\frac{\alpha}{2}\leq \mu \leq Z_\frac{\alpha}{2}) = 1- \alpha$$  

$$
\pm  Z_{\frac{\alpha}{2}} = \pm  Z_{0.975} = \pm 0.8340$$  
$$
\Rightarrow  IC = (\bar{x} \pm Z_{\frac{\alpha}{2}} \frac{\sigma}{n}) = \pm 0.8340 \frac{1}{100}$$  
$$ (-0.00834;0.008434)$$  
* Ahora con n=1000 solo cambiamos la n en la ecuación del IC.  
$$IC = (\bar{x} \pm Z_{\frac{\alpha}{2}} \frac{\sigma}{n}) = \pm 0.8340 \frac{1}{1000}$$  
$$ (-0.000834;0.0008434)$$