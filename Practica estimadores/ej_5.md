# Ejercicio 5
Considere muestras aleatorias de cada una de las siguientes distribuciones:
i. normal de parámetros $\mu$ y $\sigma^{2}$  
ii. exponencial de parámetro 𝜆;  
iii. Poisson de parámetro 𝜆;  
iv. con PDF que depende de un parámetro 𝜃 ∈ (0, 1);  

$$
f(x; \theta) = \frac{1}{\theta}x^{(\frac{1}{\theta}-1)}I_{[0,1]}(x)
$$

, donde  

$$I_{[0,1]}(x) = \begin{matrix}
1 & si\: 0\leq x\leq 1,  \\
0 & \textrm{en caso contrario} \\
\end{matrix}.
$$  

v. geométrica de parámetro 𝑝;  
vi. gamma de parámetros 𝛼 y 𝜆;  
vii. uniforme U [0, 𝜃].  
* (a) Hallar en cada caso el estimador de momentos de los parámetros
* (b) Hallar en cada caso salvo vi el estimador de máxima verosimilitud de los parámetros (salvo vi)
* (c) Para i,ii,iii y vii decir si los estimadores son insesgados o asintóticamente insesgados.
* (d) Calcular el ECM de los estimadores de 𝜃 en vii. Comparando uno con otro, ¿cuál de los dos
estimadores usarías

## Resolución 
Voy a poner como título la distribución y como items las consignas. Asi esta todos los puntos de la misma distribución juntos.  
### Normal
* **a.** En este punto nos piden el estimador de momentos de la normal.  
**Método de momentos**: La idea básica consiste en igualar ciertas características
muestrales con las correspondientes características poblacionales. Recordemos la
siguiente definición.   
Entonces para la Normal, la cual tiene 2 parámetros, llegariamos solo hasta $E(x^{2})$.  
    * Para el primer parametro: $\Rightarrow E(x^{1})=\mu$
    * Para el segundo parámetro:  

    $$ 
    E(x^{2})= Var(x) + (E(x))^{2}
    $$  

    Siendo $Var(x) = \sigma^{2}$ y $(E(x))^{2}= \mu_{n}^{2}$.  
    Despejamos la varianza asi nos queda sigma despejado.  
    $$Var(x)= E(x^{2}) - (E(x))^{2}$$  
Como es el estimador de metodo de momentos se define a un momento como: $M_1= \frac{1}{n}\sum_{i=1}^{n}x_{i}^{m}$, siendo m el numero de parametro a estimar.  
Entonces si igualamos los estimadores de momentos quedan:  
1. $$E(x^{1}) = M_1 =\mu \Rightarrow \mu=\frac{1}{n}\sum_{i=1}^{n}x_{i}$$
2. 
$$ E(x^{2}) = M_2 =\sigma^{2}+\mu^{2} \Rightarrow \sigma^{2}=\frac{1}{n}\sum_{i=1}^{n}x_{i}^{2} + (\frac{1}{n}\sum_{i=1}^{n}x_{i}^{2})
$$  

* **b.** Acá nos opiden el estimador de máxima verosimilitud, este estimador es basicamente buscar la función Likelihood a raíz de la funcion acumulad a de la distribución(le agregamos $\prod$) y depsues le aplicamos logaritmo, para finalizar la derivamos por cada parámetro y la igualamos a cero.  

$$
L(\mu,\sigma^{2})= \prod_{i=1}^{n}\frac{1}{\sqrt{2 \pi \sigma^{2}}}exp(-\frac{(x_i -\mu)^{2}}{2\sigma^{2}})
$$  

$$
L(\mu,\sigma^{2}) = (2\pi \sigma^{2})^{-n/2}exp (-\frac{1}{2\sigma^{2}}\sum_{i=1}^{n}(x_i -\mu)^{2})
$$  

Aplicamos logaritmo  

$$
l(\mu,\sigma^{2}) = -\frac{n}{2}ln(2\pi) - n\: ln(\theta)-\frac{1}{2 \sigma^{2}}\sum_{i=1}^{n}(x_i-\mu)^{2}
$$  

$$
\frac{\partial l(\mu, \sigma^{2} )}{\partial \mu} = \frac{1}{2\sigma^{2}}\sum_{i=1}^{n}2(x_i - \mu)=\frac{1}{\sigma^{2}}\sum_{i=1}^{n}(x_i - \mu) = 0
$$  

$$\Rightarrow \sum_{i=1}^{n}x_i - n\mu =0 \Rightarrow n\mu=\sum_{i=1}^{n}x_i
$$  

$$
\hat{\mu}= \frac{1}{n}\sum_{i=1}^{n}x_i
$$  

Ahora buscamos la derivada de $\sigma^{2}$

$$
\frac{\partial l(\mu, \sigma^{2} )}{\partial \sigma^{2}} = -\frac{n}{\sigma} -\sum_{i=1}^{n}(x_i -\mu)^{2}\frac{1}{\sigma^{3}}
$$  

$$
=-\frac{1}{\sigma}+\frac{1}{\sigma^{3}}\sum_{i=1}^{n}(x_i -\mu)^{2} = 0
$$  

$$
n=\frac{1}{\sigma^{2}}\sum_{i=1}^{n}(x_i -\mu)^{2} \Rightarrow \hat{\sigma^{2}} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \mu)^{2}
$$  

* c. Decir si los estimadores son insesgados o asintoticamente insesgados.  
Un estimador es insesgado cuanod la esperanza del mismo estimador es igual al parámetro.  
El estimador asintoticamente insesgado es el que la esperanza del mismo tendiendo n a infinito es igual al parámetro.  
Es decir:  
    * $E(\hat{\theta}) = \theta$ (insesgado);  
    * n->infinito : $E(\hat{\theta})= \theta$  


$E(\hat{\mu}) = \frac{1}{n} E(\sum_{i=1}^{n}x_i) = \mu$ 
Por lo tanto es insesgado.  

$(n-> \infty);\: E(\hat{\sigma^{2}})= \sigma^{2}$ Este ej esta demostrado en una de las practicas de Ale. Que ahora no tengo, depues lo copio.  





