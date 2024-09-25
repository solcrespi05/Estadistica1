# Ejericio 1
Sea 𝑋 una variable aleatoria normal de varianza conocida $\sigma^{2} = 1$ y esperanza desconocida $\mu$. Se realiza un test que decide si rechazar o preservar la hipótesis $H_0: \mu ≤ 0$ a partir de 𝑛 = 100 muestras. Para cierto 𝑐 > 0, el test dice “Dadas muestras $ 𝑥1,. . .,𝑥𝑛 $, rechazar $H_0$ si $\bar{x}> 𝑐”$. 
- (a) Encontrar el valor de 𝑐 para que el test tenga un nivel de 5%. 
- (b) Describir la región de rechazo, que es un subconjunto de R𝑛. 
- (c) Calcular la potencia que tiene el test si el verdadero valor de 𝜇 es 𝜇 = 0.1 y si es 𝜇 = 1.  

## Resolución 
- a. Planteamos las variables que tenemos:  
    - $H_0: \mu\leq 0$
    - $H_1 : \mu > 0$
    - $n=100$
    - $\sigma^{2} = 1$
    - $\alpha = 0.05$  

Tenemos entonces que el estadístico para estas características es :  

$$
Z=\frac{\bar{x}-\mu}{\frac {\sigma}{\sqrt{n}}}
$$  

Por lo que si nosotros buscamos el valor de c para que el test tenga un nivel del 5%, tomamos a $\bar{x}$ como c y reemplazom los otros valores:  

$$
Z_{1-\alpha}= Z_{1-0.05} = Z_{0.95} = 1.64
$$  

$$
\Rightarrow \ 1.64= \frac{c-0}{1/\sqrt{100}} \ \Rightarrow \ 1,64\ .\ 0,1 = c
$$  

$$
c=0,164
$$  

Por lo que si $\bar{x} > 0,164$ Rechazo $H_0$  

- b. La región de rechazo si el test tiene un nivel de 5% nos quedaria: $R = (0,164;+ \infty )$  

- c. Calculamos la potencia del test para $\mu = 0,1$:  

$$
\textrm{Potencia del test} = P(Z<Z_{vc})
$$  

Siendo $Z_{vc}$ nuestro Z de valor crítico pero a diferencia del que calculamos arriba, le cambiamosa nuestro $\mu$.  

$$
P \left(Z> \left(\frac{0,164-0,1}{1/\sqrt{100}} \right)\right) = \\ = P(Z>0,64)= \\ = 1-0,7389= \ 0,2611
$$  

Potencia del test con $\mu = 0.1$ $\rightarrow$  $0,2611$

**Si $\mu = 1$**  

$$
P \left(Z> \left(\frac{0,164-1}{1/\sqrt{100}} \right)\right) = \\ = P(Z>(-8.36)) = P(Z<8,36) \approx 1
$$  

Potencia del test con $\mu = 1$ $\rightarrow$  $\approx 1$  


