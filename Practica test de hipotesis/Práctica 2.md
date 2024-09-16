# Práctica 2

---

# **1. Planteamiento de un Test de Hipótesis**

Un test de hipótesis es un procedimiento estadístico que se utiliza para tomar decisiones sobre un parámetro poblacional, basándose en datos muestrales. El proceso generalmente sigue estos pasos:

### a) **Hipótesis Nula ($H_0$ ) y Alternativa ($H_A$):**

- **Hipótesis Nula ($H_0$)**: Es la afirmación que se supone verdadera hasta que se demuestre lo contrario. El objetivo del test es rechazar o no $H_0$  basándose en los datos observados.
- **Hipótesis Alternativa ($H_A$)**: Es la afirmación opuesta a $H_0$. Se acepta si la evidencia muestral es suficientemente fuerte para rechazar $H_0$ .

Ejemplo:

- $H_0: \mu \leq 0$
- $H_A: \mu > 0$

### b) **Estadística de Prueba:**

- Es una función de los datos muestrales que se utiliza para evaluar la hipótesis. La estadística de prueba puede seguir diferentes distribuciones dependiendo del tipo de datos y el parámetro que se esté evaluando (distribución normal, $t -student$, $\chi^2$, etc.).

### c) **Valor Crítico y Nivel de Significancia ($\alpha$):**

- **Nivel de Significancia ($\alpha$)**: Es la probabilidad máxima de cometer un **error de tipo I** (rechazar $H_0$ cuando es verdadera). Los valores comunes son $\alpha = 0.05$ o $\alpha = 0.01$.
- **Valor Crítico**: Es el punto de corte que divide la región de no rechazo de la región de rechazo. Se obtiene de la distribución de la estadística de prueba para el nivel  
 $\alpha$.

### d) **Región de Rechazo:**

- Es el conjunto de valores de la estadística de prueba que llevan al rechazo de $H_0$. Si el valor observado de la estadística de prueba cae dentro de esta región, $H_0$ es rechazada a favor de $H_A$.

Ejemplo:

- Si la estadística de prueba es la media muestral  $\bar{x}$ , la región de rechazo puede ser $\bar{x} > c$, donde  $c$ es el valor crítico calculado para el nivel de significancia.

---

# **2. Tipos de Errores en un Test de Hipótesis**

### a) **Error de Tipo I ($\alpha$ ):**

Este error ocurre cuando se rechaza la hipótesis nula $H_0$  cuando en realidad es verdadera. El nivel de significancia $\alpha$  es la probabilidad de cometer un error de tipo I.

Ejemplo: Si $\alpha = 0.05$, hay un 5% de probabilidad de rechazar $H_0$  incorrectamente.

### b) **Error de Tipo II ($\beta$):**

Este error ocurre cuando no se rechaza $H_0$ cuando en realidad es falsa (es decir, $H_A$ es verdadera). La probabilidad de cometer un error de tipo II se denota como $\beta$.

### c) **Potencia de un Test:**

La potencia de un test es la probabilidad de rechazar $H_0$ cuando $H_A$ es verdadera, es decir, $1 - \beta$ . Cuanto mayor sea la potencia, más efectivo es el test para detectar diferencias reales.

---

# **3. Pruebas de Hipótesis para la Media**

### a) **Test de Hipótesis con Varianza Conocida (Distribución Normal):**

Cuando la varianza de la población es conocida, la estadística de prueba para la media es:

$$
Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
$$

donde $\mu_0$  es el valor supuesto bajo  $H_0$ , $\bar{X}$  es la media muestral, $\sigma$  es la desviación estándar poblacional y $n$ es el tamaño de la muestra.

- Si $Z$ es mayor que el valor crítico $z_{\alpha}$  para un test unilateral a nivel $\alpha$ , se rechaza $H_0$.

### b) **Test de Hipótesis con Varianza Desconocida (Distribución t-Student):**

Si la varianza es desconocida, la estadística de prueba cambia a:

$$
t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
$$

donde $s$ es la desviación estándar muestral. Esta estadística sigue una distribución t-Student con $n - 1$  grados de libertad.

---

# **4. Test para Proporciones**

Los test para proporciones se utilizan cuando se evalúan hipótesis sobre la proporción $p$ de éxitos en una población. La estadística de prueba es:

$$
Z = \frac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0) / n}}
$$

donde:

- $\hat{p}$  es la proporción muestral de éxitos,
- $p_0$  es la proporción poblacional bajo $H_0$ ,
- $n$ es el tamaño de la muestra.

Ejemplo:

- $H_0: p = 0.2$
- $H_A: p > 0.2$

Se rechaza $H_0$  si el valor observado de $Z$  es mayor que el valor crítico $z_{\alpha}$ .

---

# **5. Test de Bondad de Ajuste**

Los test de bondad de ajuste se utilizan para verificar si los datos observados siguen una distribución específica (por ejemplo, si un dado es equilibrado o una moneda es justa).

### a) **Test $\chi^2$ :**

- Se utiliza para comparar las frecuencias observadas con las frecuencias esperadas bajo una cierta hipótesis.
- La estadística de prueba es:

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

donde $O_i$ son las frecuencias observadas y $E_i$ son las frecuencias esperadas.

Se compara el valor de $\chi^2$ con el valor crítico de la distribución $\chi^2$  con el número adecuado de grados de libertad para decidir si rechazar $H_0$.

### b) **Aplicaciones:**

- **Monedas**: Para verificar si una moneda es justa, se comparan las frecuencias de caras y cecas con la distribución esperada (50%-50%).
- **Dados**: Para verificar si un dado es equilibrado, se comparan las frecuencias de los resultados de cada cara con las frecuencias esperadas (1/6 para cada cara).

---

# **6. Interpretación del p-valor**

El **p-valor** es la probabilidad de obtener un valor de la estadística de prueba al menos tan extremo como el observado, bajo la suposición de que $H_0$ es verdadera. Si el p-valor es menor que el nivel de significancia $\alpha$ , se rechaza $H_0$.

- **p-valor bajo ($p < \alpha$ )**: Se rechaza $H_0$, lo que indica que hay suficiente evidencia para aceptar$H_A$.
- **p-valor alto ($p \geq \alpha$ )**: No se rechaza $H_0$, lo que indica que no hay suficiente evidencia para aceptar $H_A$).

---

# **7. Tamaño de la Muestra**

El **tamaño de la muestra** influye en la precisión del test de hipótesis. Un tamaño de muestra mayor:

- Reduce el error estándar de la media ($\sigma / \sqrt{n}$ ), lo que hace más fácil detectar diferencias significativas.
- Aumenta la potencia del test, ya que las diferencias reales son más detectables.

El tamaño de la muestra necesario para un test de hipótesis se puede calcular a partir de la fórmula del error estándar, los valores críticos de la distribución y la magnitud del efecto que se desea detectar.

---