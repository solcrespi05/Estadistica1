#   Ejercicio 3
Supongamos que tenemos un dataset $(𝑥1,𝑦1),..., (𝑥𝑛,𝑦𝑛)$ ∈ $R^2$ para $𝑛 ∈ N$ y hacemos un modelo de regresión lineal, donde $y_1 = \beta_0 + \beta_1 x_i + \varepsilon_i $.
(a) Mostrar que los valores de $𝛽_0$ y $𝛽_1$ que minimizan la suma de los residuos $\sum_{i=1}^{n}\varepsilon_𝑖^2$ son

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

## Demostración
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

- La derivada de $\beta_1$ queda:
$$
\frac{\partial RSS}{\partial \beta_1} = \sum_{i=1}^{n}2[y_i - (\beta_0 + \beta_1 x_i)](-x_i) = 0$$  

$$
$$
