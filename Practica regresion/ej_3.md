#   Ejercicio 3
Supongamos que tenemos un dataset $(𝑥1,𝑦1),..., (𝑥𝑛,𝑦𝑛)$ ∈ $R^2$ para $𝑛 ∈ N$ y hacemos un modelo de regresión lineal, donde $y_1 = \beta_0 + \beta_1 x_i + \varepsilon_i $.
a. Mostrar que los valores de $𝛽_0$ y $𝛽_1$ que minimizan la suma de los residuos $\sum_{i=1}^{n}\varepsilon_𝑖^2$ son

$$
\hat{\beta_1} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}
,
\hat{\beta_0}  = \bar{y}- \hat{\beta_1} \bar{x}
$$

(b) Podemos demostrar que un estimador no sesgado de 𝜎 es

$$
\hat{\sigma^2} = \frac{1}{n-2}\sum_{i=1}^{n}(y_1 - \bar{y})^2
$$

¿Cómo se interpreta el 2 que aparece restando en el denominador?

(c)¿Que pasaría si hicieramos un ajuste de la forma $𝑌 ∼ 𝛽𝑋$?

## Demostración punto a
Tenemos la ecuación de $RSS = \sum(f(x_i)-y_i)^2$ (en otras palabras:  $\sum_{i=1}^{n}\varepsilon_𝑖^2$) y la derivamos cada $\beta$ e igualamos a 0 para encontrar los $\beta_0$ y $\beta_1$ que minimizan la RSS.

entonces nos queda:
- La derivada de  $\beta_0$:  

$$\frac{\partial RSS}{\partial \beta_0} = \sum_{i=1}^{n}2\left [ y_i - (\beta_0 + \beta_1 x_i) \right ] (-1) = 0
$$  

$$\sum_{i=1}^{n}(-2)y_i - (\beta_0 + \beta_1 x_i) = 0
$$   

$$\sum_{i=1}^{n}y_i - \sum_{i=1}^{n}\beta_0 - \sum_{i=1}^{n} \beta_1 x_i = 0
$$  

$$\sum_{i=1}^{n}(y_i - \beta_1 x_i) = \sum_{i=1}^{n} \beta_0
$$  

$$n\bar{y} - \beta_1 \bar{x} n = n \beta_0
$$  

$$\beta_0= \bar{y} - \beta_1 \bar{x}
$$  

- La derivada de $\beta_1$ queda:(aca copie y pegue del [repo](https://colab.research.google.com/drive/1cYSX0Hhx8Ba-VfZAlcpCLuYBJbF9d-dC#scrollTo=uqtslOGfxd91))  

$$\frac{\partial SCR}{\partial\hat\beta_1}= -2 \sum_{i=1}^{n} x_i(y_i - \hat\beta_0 - \hat\beta_1 x_i) = 0  $$

$$\sum_{i=1}^{n} x_i y_i = \hat\beta_0 \sum_{i=1}^{n} x_i + \hat\beta_1 \sum_{i=1}^{n}x_i^2 = 0  $$

Esta es la segunda ecuación normal. Sustituyendo la primera en la segunda y definiendo $S_{xy} := \frac{1}{n} \sum_{i=1}^{n}  {(x_i - \bar x)(y_i - \bar y)}=\frac{1}{n} \sum_{i=1}^{n}x_i y_i - \bar x \bar y $ (la covarianza muestral) tenemos


$$\sum_{i=1}^{n} x_i y_i = (\bar y_n -\hat\beta_1 \bar x_n) \sum_{i=1}^{n} x_i + \hat\beta_1 \sum_{i=1}^{n}x_i^2 = 0  $$

$$ \sum_{i=1}^{n} (x_i y_i - \bar y x_i)= \hat\beta_1 \left( \sum_{i=1}^{n}(x_i^2 - \bar x_n x_i)\right) $$

Dividiendo por $n$ y operando

$$
\hat\beta_1  = \frac{S_{xy}}{S_{xx}}
$$

## Punto b
Nos pide interpretar el 2 que aparece en el denomindor del estimador insesgado de $\sigma$ :  

$$\hat{\sigma^2} = \frac{1}{n-2}\sum_{i=1}^{n}(y_1 - \bar{y})^2
$$  

El 2 que aparece en el denominador se relaciona con la cantidad de parámetros que estamos estimando, en el caso de la regresión lineal serían $\beta_0$ y $\beta_1$. Cuando estimamos esos dos parámetros se reduce el número de grados de libertad de la varianza de los errores. 
Entonces decimos que el estimador de la varianza tiene $n-2$ grados de libertad. 

## Punto c
