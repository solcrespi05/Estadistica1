#   Ejercicio 3
Supongamos que tenemos un dataset $(𝑥1,𝑦1),..., (𝑥𝑛,𝑦𝑛)$ ∈ $R^2$ para $𝑛 ∈ N$ y hacemos un modelo de regresión lineal, donde $𝑦_𝑖 = 𝛽0 + 𝛽1_𝑥_𝑖 +𝜀_𝑖$.
    (a) Mostrar que los valores de $𝛽_0$ y $𝛽_1$ que minimizan la suma de los residuos $\sum_{i=1}^{n}𝜀_𝑖$ son

    $$
    \hat{\beta_1} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}
    $$ ,
    $$ 
    \hat{\beta_0}  = \bar{y}- \hat{\beta_1} \bar{x}
    $$

    (b) Podemos demostrar que un estimador no sesgado de 𝜎 es
    $$
    \hat{\sigma^2} = \frac{1}{n-2}\sum_{i=1}^{n}(y_1 - \bar{y})^2
    $$

    ¿Cómo se interpreta el 2 que aparece restando en el denominador?
 
    (c)¿Que pasaría si hicieramos un ajuste de la forma $𝑌 ∼ 𝛽𝑋$?